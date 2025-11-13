# FreeRTOS Multitasking on Raspberry Pi Pico

## 📅 Date: 2025-11-04

### 🎯 Goal
Learn FreeRTOS fundamentals by implementing a multitasking application on the Raspberry Pi Pico.

### 📝 Description
This project demonstrates basic FreeRTOS concepts including task creation, scheduling, and inter-task delays. Two concurrent tasks run independently:
- **LED Task**: Blinks the onboard LED every 500ms
- **UART Task**: Sends log messages via USB CDC every 1 second

### 🛠️ Technical Details
- **MCU**: Raspberry Pi Pico (RP2040)
- **RTOS**: FreeRTOS Kernel
- **Port**: `portable/ThirdParty/GCC/RP2040/`
- **Build System**: CMake + Pico SDK
- **Output**: USB CDC serial for logging

### 📂 Project Structure
```
freertos-multitask/
├── src/
│   └── main.c              # Main application code
├── config/
│   └── FreeRTOSConfig.h    # FreeRTOS configuration
├── CMakeLists.txt          # Build configuration
└── pico_sdk_import.cmake   # Pico SDK integration
```

### 🚀 How to Build
```bash
cd build
cmake ..
make
```

Flash `pico_freertos.uf2` to the Pico by holding BOOTSEL while connecting USB.

### 🧠 What I Learned
- Task creation and priority management
- Task scheduling and delays (`vTaskDelay`)
- FreeRTOS integration with bare-metal projects
- How to handle missing files and build errors
- Understanding Cortex-M0+ hardware mapping
- Practical workflow: MicroPython → C → RTOS development
- USB serial debugging and monitoring

### 🔜 Next Steps
- [ ] Add `uxTaskGetSystemState()` for runtime task monitoring
- [ ] Implement queues for inter-task communication
- [ ] Add interrupt handlers with queue integration
- [ ] Connect real sensors and simulate data flow
- [ ] Explore semaphores and mutexes

### 📊 Task Details
| Task | Priority | Delay | Function |
|------|----------|-------|----------|
| LED  | 1        | 500ms | Toggle onboard LED |
| UART | 1        | 1000ms | Print system status |

### 🔧 Debugging
Monitor output via serial:
```bash
screen /dev/ttyACM0
```

Or use minicom:
```bash
minicom -D /dev/ttyACM0 -b 115200
```
