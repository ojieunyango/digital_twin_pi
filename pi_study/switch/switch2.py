import RPi.GPIO as gpio
from time import sleep

swPin = 13

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)




prevState = gpio.LOW

try:
    while True:
        swState = gpio.input(swPin)
        if swState == gpio.HIGH and prevState == gpio.LOW:
            print(1)
        prevState = swState
        sleep(0.05)
        


except KeyboradInterrupt:
    pass
finally:
    gpio.cleanup()