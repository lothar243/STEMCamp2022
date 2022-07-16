from gpiozero import LED
from time import sleep
from threading import Thread
from pprint import pprint

# matching the pin number on the LED matrix to the GPIO pin on the pi
# Example: Matrix Pin 1 (For R5) is controlled by GPIO6
pins = {1: 6,   # R5
        2: 5,   # R7
        5: 0,   # R8
        7: 11,  # R6
        8: 9,   # R3
        9: 13,  # R1
        12: 19, # R4
        14: 26, # R2
        16: 21, # C8
        15: 20, # C7
        13: 16, # C1
        11: 12, # C6
        10: 7,  # C4
        3: 8,   # C2
        4: 25,  # C3
        6: 24   # C5
        }
leds = {}
for pin, gpio in pins.items():
    leds[pin] = LED(gpio)

currentBitmap = [[False] * 8 ] * 8

vert = [13, 3, 4, 11, 6, 10, 15, 16]
hori = [9, 14, 8, 12, 1, 7, 2, 5]

def displayNumber(num):
    for exp in range(0,64):
        pass

def momentaryDisplay(bitmap):
    """Takes a 2d list of boolean values and turns lights on for each True value"""
    for row in range(8):
        leds[hori[row]].on()
        for col in range(8):
            if bitmap[row][col]:
                leds[vert[col]].off()
        sleep(.001)
        for col in range(8):
            leds[vert[col]].on()
        leds[hori[row]].off()

class myThread(Thread):
    def __init__(self, threadID, name):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            momentaryDisplay(currentBitmap)



for pin in vert:
    leds[pin].on()

thread1 = myThread(1, "Thread-1")
thread1.start()

while(True):
    for framenum in range(8):
        mybitmap = [[False] * 8] * 8
        mybitmap[0][framenum] = True
        currentBitmap = mybitmap
        print(f"{framenum=}")
        pprint(currentBitmap)
        sleep(.4)
    for framenum in range(8):
        mybitmap = [[False] * 8] * 8
        mybitmap[framenum] = ([True] * 8)
        currentBitmap = mybitmap
        print(f"{framenum=}")
        pprint(currentBitmap)
        sleep(.4)




