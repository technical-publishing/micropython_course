from micropython import const
from machine import Pin
import time

PIN_0 = const(0)

isr_flag = False
pin0= Pin(PIN_0, Pin.IN)

def p0_isr(pin):
    global isr_flag
    isr_flag = not isr_flag

pin0.irq(handler=p0_isr, trigger=Pin.IRQ_FALLING)

while True:
    print("Flag ist: {}".format(isr_flag))
    time.sleep(1)
    