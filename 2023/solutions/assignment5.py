from microbit import *
import radio

# Initialize radio and variables
radio.on()
radio.config(channel=15)
user_choice = ''
opponent_choice = ''

while True:
    display.clear()
    
    # Make your choice
    if button_a.was_pressed():
        user_choice = 'rock'
        radio.send('rock')
    elif button_b.was_pressed():
        user_choice = 'scissors'
        radio.send('scissors')
    elif accelerometer.was_gesture('shake'):
        user_choice = 'paper'
        radio.send('paper')
    
    # Receive opponent's choice
    incoming = radio.receive()
    if incoming:
        opponent_choice = incoming
    
    # If both choices are made, then compare
    if user_choice and opponent_choice:
        if user_choice == opponent_choice:
            display.show(Image.HAPPY)
        elif (user_choice == 'rock' and opponent_choice == 'scissors') or \
             (user_choice == 'scissors' and opponent_choice == 'paper') or \
             (user_choice == 'paper' and opponent_choice == 'rock'):
            display.show(Image.YES)
        else:
            display.show(Image.NO)
        
        sleep(2000)
        
        # Reset choices for next round
        user_choice = ''
        opponent_choice = ''
