from microbit import *
import random

while True:
    user_choice = ''
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    if button_a.is_pressed():
        user_choice = 'rock'
    elif button_b.is_pressed():
        user_choice = 'scissors'
    elif accelerometer.was_gesture('shake'):
        user_choice = 'paper'
    
    if user_choice:
        if user_choice == computer_choice:
            display.show(Image.HAPPY)
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            display.show(Image.YES)
        else:
            display.show(Image.NO)
        
        sleep(2000)
        display.clear()
