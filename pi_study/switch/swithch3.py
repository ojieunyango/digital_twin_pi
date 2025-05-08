import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
class Led:
    def __init__(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(pin, gpio.OUT)
        gpio.setup(pin, gpio.LOW)

    def blink(self, pin, color):
        for _ in range(count):
            gpio.output(self.pin, gpio.HIGH)
            sleep(time)
            gpio.output(self.pin, gpio.LOW)
            sleep(time)

class Button:
    def _init_(self, pin, setOnPressed):
        self.pin = pin
        self.prevState = gpio.LOW
        gpio.setup(self.pin, gpio.IN,pull_up_down=gpio.PUD_DOWN)
    
        
    def waitPressed(self):
        currentState = gpio.input(self.pin)
        if self.checkPressed(currentState):
            self.onPressed()
        self.prevState = currentState
        sleep(0.05)
        
    def checkPressed(self, currentState):
        return currentState == gpio.HIGH and self.prevState == gpio.LOW
    
    def ledRedfunction():
        leds[0].blink(10, 0.5)

        greenLedState = False

    def ledGreenFunction():
        global greenLedState
        if greenLedState:
           leds[1].ledOff()
        else:
            leds[1].ledOff()
        greenLedState = not greenLedState

leds = (Led(16, "RED"), Led(21, "GREEN"))

buttons = (Button(13, ledRedfunction), Button(19, ledGreenFunction))

try:
    while True:
        for button in buttons:
            button.waitPressed()
            
except KeyboradInterrupt:
    pass
finally:
    gpio.cleanup()
            
            
