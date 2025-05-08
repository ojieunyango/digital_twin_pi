import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 20, 21)
#BCM -> GPIO핀번호
#BOARD -> BOARD기판번호
gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)

try:
    isOnAll = False
    while True:
       for pin in ledPin:
           if isOnAll:
               gpio.output(pin, gpio.LOW)
           else:
               gpio.output(pin, gpio.HIGH)
           sleep(0.1)
        isOnAll = not isOnAll
       

    