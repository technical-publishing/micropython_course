from machine import UART
import utime

uart = UART(2, 9600)                

while True:
    for counter in range(10):
        uart.write(str(counter))
        utime.sleep_ms(100)
    