import esp32
import utime


while True:
    temp = (esp32.raw_temperature() - 32) * 5.0/9.0
    print(temp)
    utime.sleep(1)


