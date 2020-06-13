from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

pin16 = Pin(16, Pin.OUT)
pin16.on()

i2c = I2C(scl=Pin(15), sda=Pin(4))

oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)

oled.rect(10, 10, 20, 10, 1)
oled.show()