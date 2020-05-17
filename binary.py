from gpiozero import LED, Button, LEDBoard
from time import sleep
from random import randint, shuffle

numbers = [
    (22, '10110'),
    (43, '101011'),
    (66, '1000010'),
    (19, '10011')
    
]

shuffle(numbers)

button_check = Button(24)
led_good = LED(25)
led_bad = LED(9)
button1 = Button(2)
button0 = Button(16)
answer = str()

for number in numbers:
    answer = str()
    decimal_number, binary_number = number
    print(decimal_number)
    while True:
        if button0.is_pressed:
            answer += '0'
            print(answer)
            sleep(0.2)
        if button1.is_pressed:
            answer += '1'
            print(answer)
            sleep(0.2)
        if button_check.is_pressed:
            if answer == binary_number:
                print('Good work!')
                led_good.on()
                sleep(0.5)
                led_good.off()
            else:
                print('Correct answer was:', binary_number) 
                print('Next question will be easier')
                led_bad.on()
                sleep(0.5)
                led_bad.off()
            sleep(0.5)
            break