from microbit import *

while True:
    for i in range(5):
        for j in range(5):
            display.set_pixel(j, i, 9)
            sleep(200)
            display.clear()