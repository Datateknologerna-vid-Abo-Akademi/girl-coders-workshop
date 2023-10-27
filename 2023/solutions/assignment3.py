from microbit import *

while True:
    temp = temperature()
    
    if temp > 30:
        display.show(Image.SKULL)
        sleep(1500)
    elif temp < 10:
        display.show(Image.XMAS)
        sleep(1500)
    else:
        display.scroll(str(temp) + "C")
    
    sleep(2000)
    display.clear()