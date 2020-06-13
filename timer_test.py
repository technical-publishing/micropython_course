from machine import Timer
import utime

def timer_isr(timer):
    print("ISR ausgeführt")
    print(timer)

timer = Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=timer_isr)

while True:
    for i in range(10000):
        print("Der Wert von {} ist: ".format(i))
        utime.sleep_ms(100)