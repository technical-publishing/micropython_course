from machine import DAC, Pin
import utime

da = DAC(Pin(26))
da.write(0)

