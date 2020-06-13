from machine import Pin, I2C, UART
from ssd1306 import SSD1306_I2C
import utime

#uart = UART(2, 9600)
pin16 = Pin(16, Pin.OUT)
pin16.on()
i2c = I2C(scl=Pin(15), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(1)

#def print_oled(value):
#    #led.on()
#    #pin16.init(mode=pin16.OUT)
#    #pin16.on()
#    utime.sleep_ms(500)
#    oled.fill(1)
#    oled.text('Wert ist: {}'.format(value), 10, 10, 1)
#    pin16.init(mode=pin16.IN)
#    #led.off()


while True:
    #counter = uart.readline()
    #if counter is not None:
    for counter in range(10):
#        print_oled(counter)
        utime.sleep(1)




