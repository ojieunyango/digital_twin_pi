import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)


BUTTONS = {
    13: '1',
    19: '2',
    26: '3'
}


LEDS = {
    '1': 16,
    '2': 20,
    '3': 21
}

NUMBERS = ['1', '2', '3']
input_sequence = []

# 모든 핀 설정
for pin in BUTTONS:
    gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
for pin in LEDS.values():
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.LOW)


# 버튼 클래스 정의
class Button:
    def __init__(self, pin, onPressed):
        self.pin = pin
        self.prevState = gpio.LOW
        self.onPressed = onPressed

    def waitPressed(self):
        currentState = gpio.input(self.pin)
        if self.checkPressed(currentState):
            self.onPressed()
        self.prevState = currentState
        sleep(0.05)

    def checkPressed(self, currentState):
        return currentState == gpio.HIGH and self.prevState == gpio.LOW


# 버튼이 눌렸을 때 호출될 함수 생성 함수
def make_button_handler(button_num):
    def handle_press():
        print(f"버튼 {button_num} 눌림")

        # LED 켜기
        gpio.output(LEDS[button_num], gpio.HIGH)
        sleep(0.3)
        gpio.output(LEDS[button_num], gpio.LOW)

        # 입력 추가
        input_sequence.append(button_num)

        # 입력 초과 시 앞에서 자르기
        if len(input_sequence) > len(NUMBERS):
            input_sequence.pop(0)

        print("입력 상태:", input_sequence)

        # 비밀번호 확인
        if input_sequence == PASSWORD:
            print("비밀번호 일치! 문을 엽니다. 🔓")
            # 모든 LED 반짝이기
            for _ in range(3):
                for pin in LEDS.values():
                    gpio.output(pin, gpio.HIGH)
                sleep(0.2)
                for pin in LEDS.values():
                    gpio.output(pin, gpio.LOW)
                sleep(0.2)
            input_sequence.clear()

    return handle_press


# 버튼 객체 생성
buttons = [Button(pin, make_button_handler(num)) for pin, num in BUTTONS.items()]

try:
    while True:
        for button in buttons:
            button.waitPressed()

except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()
