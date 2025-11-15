# BME280 Temperature, Humidity & Pressure Sensor

## 📅 Date: 2025-11-15

### 🎯 Goal
Learn I2C communication by connecting and reading data from a BME280 environmental sensor.

### 🛠️ Hardware Setup

**Components:**
- Raspberry Pi Pico
- BME280 sensor module
- 4 jumper wires

**Wiring:**

| BME280 Pin | Wire  | Pico Pin | Function |
|------------|-------|----------|----------|
| VIN        | Red   | 3V3(OUT) | Power    |
| GND        | White | GND      | Ground   |
| SDA        | Blue  | GP2      | I2C Data |
| SCL        | Yellow| GP3      | I2C Clock|

**I2C Bus:** I2C1 on GP2 (SDA) and GP3 (SCL)

### ⚠️ Important Notes

**MicroPython I2C Pin Restrictions:**
- I2C0: GP0 (SDA), GP1 (SCL)
- I2C1: GP2 (SDA), GP3 (SCL)

Initial attempt used GP4/GP9 which are **not supported** by MicroPython for I2C.  
C SDK allows flexible I2C pin routing, but MicroPython does not.

### 📝 Implementation

**Language:** MicroPython  
**Libraries:** `machine.I2C`, custom `bme280.py` driver

### 🔧 Files

- `main.py` - Main program to read and display sensor data
- `bme280.py` - BME280 driver library for MicroPython

### 🚀 How to Run

1. Flash MicroPython firmware to Pico (if not already done)
2. Upload `bme280.py` to Pico root directory using Thonny
3. Upload and run `main.py`
4. View output in Thonny console or serial monitor

### 📊 Output Example

```
Temperature: 21.34 C
Pressure: 997.12 hPa
Humidity: 34.80 %
```

Data refreshes every 1 second.

### 🧠 What I Learned

- **I2C Protocol**: Two-wire communication (SDA/SCL)
- **Soldering**: Clean solder joints for reliable connections
- **Pin Configuration**: MicroPython has strict I2C pin requirements
- **Troubleshooting**: 
  - Initial error: `ValueError: bad SCL pin`
  - Cause: GP4/GP9 not supported for I2C in MicroPython
  - Solution: Moved wires to GP2/GP3
- **Sensor Calibration**: BME280 uses factory calibration data
- **Data Formatting**: Converting raw ADC values to physical units

### 🔍 Technical Details

- **I2C Address**: 0x76 (default)
- **I2C Frequency**: 100 kHz
- **Sensor Measurements**:
  - Temperature: ±1°C accuracy
  - Humidity: ±3% accuracy
  - Pressure: ±1 hPa accuracy

### 🔜 Next Steps

- [ ] Log sensor data to SD card
- [ ] Display data on OLED screen
- [ ] Send data over UART to another device
- [ ] Implement data filtering/averaging
- [ ] Add data visualization (graphs)
- [ ] Port to C SDK for more control
- [ ] Integrate with FreeRTOS for real-time data logging

### 📸 Photos

Hardware connection verified and tested successfully.

---

**Status:** ✅ Working  
**Difficulty:** Beginner  
**Time Spent:** ~2 hours (including troubleshooting)
