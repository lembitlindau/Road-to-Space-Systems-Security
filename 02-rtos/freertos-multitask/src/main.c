#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"
#include "FreeRTOS.h"
#include "task.h"

#define LED_TASK_PRIORITY  (tskIDLE_PRIORITY + 1)
#define UART_TASK_PRIORITY (tskIDLE_PRIORITY + 1)
#define LED_TASK_STACK     configMINIMAL_STACK_SIZE
#define UART_TASK_STACK    (configMINIMAL_STACK_SIZE + 128)

static void led_task(void *param) {
    const uint led_pin = PICO_DEFAULT_LED_PIN;
    gpio_init(led_pin);
    gpio_set_dir(led_pin, GPIO_OUT);

    while (true) {
        gpio_xor_mask(1u << led_pin);
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

static void uart_task(void *param) {
    (void)param;

    uart_inst_t *uart = uart0;
    const uint tx_pin = PICO_DEFAULT_UART_TX_PIN;
    const uint rx_pin = PICO_DEFAULT_UART_RX_PIN;

    uart_init(uart, 115200);
    gpio_set_function(tx_pin, GPIO_FUNC_UART);
    gpio_set_function(rx_pin, GPIO_FUNC_UART);
    uart_set_hw_flow(uart, false, false);
    uart_set_format(uart, 8, 1, UART_PARITY_NONE);
    uart_set_fifo_enabled(uart, true);

    uint32_t counter = 0;
    while (true) {
        char buffer[64];
        int len = snprintf(buffer, sizeof buffer,
                           "Tick %lu | Free heap %lu bytes\r\n",
                           (unsigned long)counter++,
                           (unsigned long)xPortGetFreeHeapSize());
        if (len > 0) {
            uart_write_blocking(uart, (const uint8_t *)buffer, (size_t)len);
        }
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

void vApplicationMallocFailedHook(void) {
    panic("Malloc failed");
}

void vApplicationStackOverflowHook(TaskHandle_t task, char *name) {
    (void)task;
    panic("Stack overflow in task %s", name);
}

int main(void) {
    stdio_init_all();

    xTaskCreate(led_task, "LED",  LED_TASK_STACK,  NULL, LED_TASK_PRIORITY,  NULL);
    xTaskCreate(uart_task, "UART", UART_TASK_STACK, NULL, UART_TASK_PRIORITY, NULL);

    vTaskStartScheduler();

    while (true) {
        tight_loop_contents();
    }
}
