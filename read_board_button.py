from machine import Pin
import time

pin9 = Pin(0, Pin.IN)

while True:
    print(pin9.value())
    time.sleep(1)
    