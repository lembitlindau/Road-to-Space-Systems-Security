cmake_minimum_required(VERSION 3.24)

set(PICO_SDK_FETCH_FROM_GIT OFF)
set(PICO_SDK_PATH ${CMAKE_CURRENT_LIST_DIR}/pico-sdk)
set(FREERTOS_KERNEL_PATH ${CMAKE_CURRENT_LIST_DIR}/freertos_kernel)
set(FREERTOS_PORT GCC_RP2040 CACHE STRING "" FORCE)
set(FREERTOS_HEAP 4 CACHE STRING "" FORCE)

include(pico_sdk_import.cmake)

project(pico_freertos_led_uart C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

add_library(freertos_config INTERFACE)
target_include_directories(freertos_config SYSTEM INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/config
)

add_subdirectory(${FREERTOS_KERNEL_PATH} freertos_kernel)

add_executable(pico_freertos
    src/main.c
)

target_link_libraries(pico_freertos
    pico_stdlib
    hardware_uart
    freertos_kernel
    freertos_config
)

pico_enable_stdio_usb(pico_freertos 0)
pico_enable_stdio_uart(pico_freertos 1)
pico_add_extra_outputs(pico_freertos)
