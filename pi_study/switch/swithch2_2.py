import RPi.GPIO as gpio
from time import sleep

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
    
    def open():
        print("문을 연다.")
    def close():
        print("문을 닫는다.")
    
buttons = (Button(13, open), Button(19, close))

try:
    while True:
        for button in buttons:
            button.waitPressed()
            
except KeyboradInterrupt:
    pass
finally:
    gpio.cleanup()
            
            
