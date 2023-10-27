from microbit import *

sequence = []
correct_sequence = ['A', 'B', 'A', 'B']

while True:
    if button_a.is_pressed():
        sequence.append('A')
        sleep(200)
    if button_b.is_pressed():
        sequence.append('B')
        sleep(200)
    
    if len(sequence) >= 4:
        if sequence[-4:] == correct_sequence:
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
        
        sequence = []
        sleep(1000)
        display.clear()