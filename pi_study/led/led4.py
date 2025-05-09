import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)

currentPassword = None

while True:
    newPassword = input("new password: ")
    confirmPassword = input("confirm password: ")
    if newPassword == confirmPassword:
        currentPassword = newPassword
        print("비밀번호가 설정되었습니다.")
        break
    else:
        print("비밀번호가 일치하지 않습니다.")

while True:
    loginPassword = input("login password: ")
    if loginPassword == currentPassword:
        gpio.output(ledPin[1], gpio.HIGH)
        break
    else:
        for i in range(5):
            gpio.output(ledPin[0], gpio.HIGH)
            sleep(0.1)
            gpio.output(ledPin[0], gpio.LOW)
            sleep(0.1)
"""
new password: 0507
confirm password: 1234
비밀번호가 일치하지 않습니다.
new password: 0507
confirm password: 0507
비밀번호가 설정되었습니다.

login passowrd: 1234
비밀번호 불일치시 빨간색 LED 5번(0.1초) 점등
login password: 0507
비밀번호 일치시 초록색 LED 계속 점등
프로그램 종료(while문 종료)
"""