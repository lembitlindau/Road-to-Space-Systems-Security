# Road to Space Systems Security

> My journey from microcontrollers to space systems — learning embedded systems, RTOS, and cybersecurity from the ground up.

![Road to Space Systems Security](assets/road-to-space-stack.png)

## 🎯 Learning Path

This repository documents my progression through embedded systems development:

1. **Bare Metal** (C / Assembly): Direct hardware control, GPIO/I2C/SPI, interrupts and registers
2. **RTOS** (FreeRTOS / Zephyr): Multiple threads/tasks, precise timing, scheduling and real-time concepts
3. **Embedded Linux** (Buildroot / Yocto): Filesystems, kernels, services, networking (TCP/IP, SSH, TLS, CAN)
4. **Space Systems & Cybersecurity**: RTEMS / VxWorks / QNX, CCSDS/SpaceWire, Secure Boot, cryptography

## � Repository Structure

```
├── 01-bare-metal/          # Bare metal projects (GPIO, interrupts, peripherals)
├── 02-rtos/                # Real-Time OS projects
│   └── freertos-multitask/ # FreeRTOS multitasking example
├── 03-embedded-linux/      # Linux-based embedded projects
├── 04-space-systems/       # Space systems and security projects
├── assets/                 # Images and diagrams
└── README.md              # This file
```

## 🚀 Projects

### 01-bare-metal — Bare Metal Programming

#### [BME280 I2C Sensor](01-bare-metal/bme280-i2c/) — 2025-11-15
Environmental sensor (temperature, humidity, pressure) using I2C communication.
- **Tech**: MicroPython, I2C protocol, BME280
- **Features**: Real-time sensor readings, calibrated measurements
- **Learned**: I2C communication, soldering, MicroPython pin restrictions, troubleshooting

### 02-rtos — Real-Time Operating Systems

#### [FreeRTOS Multitasking](02-rtos/freertos-multitask/) — 2025-11-04
First RTOS project implementing concurrent tasks on Raspberry Pi Pico.
- **Tech**: FreeRTOS, RP2040, CMake, Pico SDK
- **Features**: LED blinking task, UART logging task, USB CDC output
- **Learned**: Task creation, scheduling, delays, FreeRTOS integration

## 📚 Resources & References

- [Raspberry Pi Pico Documentation](https://www.raspberrypi.com/documentation/microcontrollers/)
- [FreeRTOS Documentation](https://www.freertos.org/Documentation/RTOS_book.html)
- [Pico SDK](https://github.com/raspberrypi/pico-sdk)

## 🛠️ Development Environment

- **Hardware**: Raspberry Pi Pico (RP2040)
- **OS**: Linux (Ubuntu/Debian)
- **Tools**: CMake, GCC ARM, Pico SDK, screen/minicom
- **Languages**: C, Assembly (future), Python (testing)

## 📈 Progress Timeline

- **2025-11-15**: BME280 I2C sensor communication ✅
- **2025-11-04**: FreeRTOS multitasking basics ✅
- **Next**: Queues, semaphores, interrupts, sensor integration with RTOS
- **Future**: Embedded Linux exploration
- **Future**: Space systems security

