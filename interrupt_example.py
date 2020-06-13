from micropython import const
from machine import Pin
import time

PIN_0 = const(0)
int_pin = 99 #globale Variable, um den Pin zu speichern
isr_flag = False #Flags müssen immer im globalen Bereich definiert werden
pin0= Pin(PIN_0, Pin.IN) #Pin als Eingang, der interne Button liegt auf D0 und der ist normalerweise high


def p0_isr(pin):
    isr_flag = not isr_flag
    int_pin = pin

pin0.irq(handler=p0_isr, trigger=Pin.IRQ_FALLING)

while True:
    print("Flag ist jetzt {}, Interrupt auf {}".format(isr_flag, int_pin))
    time.sleep(1)
    