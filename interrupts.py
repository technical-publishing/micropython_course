from micropython import const
from machine import Pin
import time

PIN_0 = const(0)
int_pin = 99
isr_flag = False

pin0 = Pin(PIN_0, Pin.IN)

def p0_isr(pin):
    global isr_flag
    global int_pin
    int_pin = pin
    isr_flag = not isr_flag

pin0.irq(handler=p0_isr, trigger=Pin.IRQ_FALLING)

while True:
    print("Flag ist jetzt {}, Interrupt auf {}".format(isr_flag, int_pin))
    time.sleep(1)