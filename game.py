from gpiozero import LED, Button, LEDBoard
from time import sleep
from random import randint

led = LED(25)
led_blue = LED(3)
led_yellow = LED(21)
blue = Button(2)
yellow = Button(16)
time_before = randint(3, 7)
blue_pressed = False
yellow_pressed = False
blue_points = 0
yellow_points = 0

print('Start')
led.off()
led_blue.off()
led_yellow.off()


for i in range(9):
    print('Round', i, 'score:', yellow_points, blue_points)
    sleep(time_before)
    led.on()

    while True:
        if blue.is_pressed:
            print('Blue is first!')
            led_blue.on()
            blue_points += 1
            sleep(2)
            led_blue.off()
            break
        if yellow.is_pressed:
            print('Yellow is first!')
            led_yellow.on()
            yellow_points += 1
            sleep(2)
            led_yellow.off()
            break
    led.off()

led.off()
print('Final score:', yellow_points, blue_points)
if blue_points > yellow_points:
    print('BLUE WINS!!!')
else:
    print('YELLOW WINS!!!')