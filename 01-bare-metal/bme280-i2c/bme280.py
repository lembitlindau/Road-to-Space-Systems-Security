# MicroPython BME280 Driver
# Supports temperature, humidity, and pressure readings via I2C

import time
from machine import I2C

class BME280:
    def __init__(self, i2c, address=0x76):
        self.i2c = i2c
        self.address = address
        self._load_calibration()
        self._set_config()

    def _load_calibration(self):
        """Load calibration data from sensor's EEPROM"""
        data = self.i2c.readfrom_mem(self.address, 0x88, 26) + \
               self.i2c.readfrom_mem(self.address, 0xE1, 7)

        # Temperature calibration
        self.dig_T1 = data[1] << 8 | data[0]
        self.dig_T2 = self._twos_comp(data[3] << 8 | data[2], 16)
        self.dig_T3 = self._twos_comp(data[5] << 8 | data[4], 16)

        # Pressure calibration
        self.dig_P1 = data[7] << 8 | data[6]
        self.dig_P2 = self._twos_comp(data[9] << 8 | data[8], 16)
        self.dig_P3 = self._twos_comp(data[11] << 8 | data[10], 16)
        self.dig_P4 = self._twos_comp(data[13] << 8 | data[12], 16)
        self.dig_P5 = self._twos_comp(data[15] << 8 | data[14], 16)
        self.dig_P6 = self._twos_comp(data[17] << 8 | data[16], 16)
        self.dig_P7 = self._twos_comp(data[19] << 8 | data[18], 16)
        self.dig_P8 = self._twos_comp(data[21] << 8 | data[20], 16)
        self.dig_P9 = self._twos_comp(data[23] << 8 | data[22], 16)

        # Humidity calibration
        self.dig_H1 = data[25]
        data = self.i2c.readfrom_mem(self.address, 0xA1, 1) + \
               self.i2c.readfrom_mem(self.address, 0xE1, 7)

        self.dig_H2 = self._twos_comp(data[1] << 8 | data[0], 16)
        self.dig_H3 = data[2]
        self.dig_H4 = self._twos_comp((data[3] << 4) | (data[4] & 0x0F), 12)
        self.dig_H5 = self._twos_comp((data[5] << 4) | (data[4] >> 4), 12)
        self.dig_H6 = self._twos_comp(data[6], 8)

    def _twos_comp(self, val, bits):
        """Convert to two's complement for signed values"""
        if val & (1 << (bits - 1)):
            val -= 1 << bits
        return val

    def _set_config(self):
        """Configure sensor for continuous measurement"""
        # Humidity oversampling x1
        self.i2c.writeto_mem(self.address, 0xF2, b'\x01')
        # Temperature and pressure oversampling x1, normal mode
        self.i2c.writeto_mem(self.address, 0xF4, b'\x27')

    @property
    def values(self):
        """Read and return formatted temperature, pressure, and humidity"""
        data = self.i2c.readfrom_mem(self.address, 0xF7, 8)

        # Extract raw ADC values
        adc_p = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
        adc_t = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
        adc_h = (data[6] << 8) | data[7]

        # Compensate (calibrate) readings
        t = self._compensate_T(adc_t)
        p = self._compensate_P(adc_p)
        h = self._compensate_H(adc_h)

        return (
            "{:.2f} C".format(t),
            "{:.2f} hPa".format(p / 100),
            "{:.2f} %".format(h)
        )

    def _compensate_T(self, adc_T):
        """Compensate temperature reading using calibration data"""
        var1 = (adc_T / 16384.0 - self.dig_T1 / 1024.0) * self.dig_T2
        var2 = ((adc_T / 131072.0 - self.dig_T1 / 8192.0) ** 2) * self.dig_T3
        self.t_fine = var1 + var2
        return (var1 + var2) / 5120.0

    def _compensate_P(self, adc_P):
        """Compensate pressure reading using calibration data"""
        var1 = self.t_fine / 2.0 - 64000.0
        var2 = var1 * var1 * self.dig_P6 / 32768.0
        var2 = var2 + var1 * self.dig_P5 * 2.0
        var2 = var2 / 4.0 + self.dig_P4 * 65536.0
        var1 = (self.dig_P3 * var1 * var1 / 524288.0 + self.dig_P2 * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * self.dig_P1

        if var1 == 0:
            return 0

        p = 1048576.0 - adc_P
        p = ((p - var2 / 4096.0) * 6250.0) / var1
        var1 = self.dig_P9 * p * p / 2147483648.0
        var2 = p * self.dig_P8 / 32768.0
        return p + (var1 + var2 + self.dig_P7) / 16.0

    def _compensate_H(self, adc_H):
        """Compensate humidity reading using calibration data"""
        h = self.t_fine - 76800.0
        h = (adc_H - (self.dig_H4 * 64.0 + self.dig_H5 / 16384.0 * h)) * \
            (self.dig_H2 / 65536.0 * (1.0 + self.dig_H6 / 67108864.0 * h *
                                      (1.0 + self.dig_H3 / 67108864.0 * h)))
        h = h * (1.0 - self.dig_H1 * h / 524288.0)
        return max(0, min(100, h))
