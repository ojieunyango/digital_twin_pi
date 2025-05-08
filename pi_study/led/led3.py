import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 20)
#BCM -> GPIO핀번호
#BOARD -> BOARD기판번호
gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)
    
currentPassword = None

while True:
      password = input("new password: ")
      cpassword = input("confirm password: ")
      if password == cpassword:
         currentPassword = password
         print("비밀번호가 설정되었습니다.")
         break
      else:
          print("비밀번호가 일치하지않습니다.")
             
while True:
      login = input("login password: ")
    
      if login == currentPassword:
          gpio.output(ledPin[1], gpio.HIGH)
          break
      else:
           for i in range(5):
             gpio.output(ledPin[0], gpio.HIGH)
             sleep(0.1)
             gpio.output(ledPin[0], gpio.HIGH)
             sleep(0.1)

        
            
        
    