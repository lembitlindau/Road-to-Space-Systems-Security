# Road to Space Systems Security

![Road to Space Systems Security]

This image illustrates the learning path and hierarchy of topics to study:
- Bare Metal (C / Assembly): direct hardware control, GPIO/IC/SPI, interrupts and registers — e.g., Raspberry Pi Pico, STM.
- RTOS (FreeRTOS / Zephyr): multiple threads/tasks, precise timing, scheduling and real-time concepts.
- Embedded Linux (Buildroot / Yocto): filesystems, kernels, services, networking (TCP/IP, SSH, TLS, CAN), kernel builds and drivers.
- Space Systems & Cybersecurity: RTEMS / VxWorks / QNX on satellites, Yocto/Linux for ground segments and payload operations, CCSDS/SpaceWire and security measures (Secure Boot, AppArmor, cryptography).

## 📅 2025-11-04 — MicroPython → C → FreeRTOS on Raspberry Pi Pico

### 🎯 Goal
Start hands-on learning of RTOS fundamentals on microcontrollers by building a FreeRTOS-based multitasking example on the Raspberry Pi Pico.

### ✅ What I did
- Got `blink.py` running with MicroPython for quick testing
- Set up the Pico SDK and compiled first C project using CMake
- Created clean project structure: `main.c + CMakeLists.txt + build/`
- Integrated FreeRTOS manually:
  - Cloned the official `FreeRTOS-Kernel` repository
  - Used the `portable/ThirdParty/GCC/RP2040/` port
  - Created and configured `FreeRTOSConfig.h`
- Implemented a multitasking example:
  - `led_task`: blinks onboard LED every 500 ms
  - `uart_task`: sends log messages every 1 second via USB CDC
- Compiled `.uf2` using `cmake` and `make`, flashed to Pico
- Verified output using `screen /dev/ttyACM0` on Linux

### 🧠 What I learned
- The basics of FreeRTOS: tasks, priorities, delays
- FreeRTOS integration into bare-metal C projects
- How to handle missing files and build errors (e.g. `port.c`, `FreeRTOSConfig.h`)
- Understanding of how FreeRTOS maps to Cortex-M0+ hardware (Pico)
- Practical workflow for switching from MicroPython to C/RTOS development
- How to use USB serial to monitor system behavior

### 🔜 Next steps
- Add `uxTaskGetSystemState()` to log task runtime info
- Implement queues between tasks (e.g. sensor → logger)
- Introduce interrupt handlers that push data to queues
- Connect a real sensor and simulate real-time task communication

---

