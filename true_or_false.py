from gpiozero import LED, Button, LEDBoard
from time import sleep
from random import randint, shuffle

questions = [
    ('1+1=2', True),
    ('1+1=3', False),
    ('"przepraszam" means "sorry"', True),
    ('"kwiat" meens "hello"', False),
    ('256*256=32768', False),
    ('256*128=32768', True),
    ('256*256=65536', True)
]

shuffle(questions)


points = 0
led_good = LED(25)
led_bad = LED(9)
button_false = Button(16)
button_true = Button(2)
max_points = len(questions)

print('Yellow = false, blue = true')

for question in questions:
    text, correct_answer = question
    print(text)
    while True:
        if button_true.is_pressed:
            answer = True
            break
        if button_false.is_pressed:
            answer = False
            break
    if answer == correct_answer:
        print('Good work!')
        led_good.on()
        sleep(0.8)
        led_good.off()
        points += 1
    else:
        print('YOU NEED TO LEARN MORE!!! IT WAS EASY!!!')
        led_bad.on()
        sleep(0.8)
        led_bad.off()
    sleep(0.3)

print('You have', points, '/', max_points, 'points')