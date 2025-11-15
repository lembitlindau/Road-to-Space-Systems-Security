from machine import Pin, I2C
import time
import bme280

# I2C1 configuration
# GP2 = SDA (blue wire)
# GP3 = SCL (yellow wire)
i2c = I2C(1, 
          scl=Pin(3),
          sda=Pin(2),
          freq=100000)

# Initialize BME280 sensor
sensor = bme280.BME280(i2c=i2c)

print("BME280 Environmental Sensor")
print("="*40)
print()

# Main loop - read and display sensor data every second
while True:
    temp, pressure, humidity = sensor.values
    print("Temperature:", temp)
    print("Pressure:", pressure)
    print("Humidity:", humidity)
    print("-" * 40)
    time.sleep(1)
