from gpiozero import LED
from time import sleep


data = LED(26)
latch = LED(19)
clock = LED(13)
clockTime = .01
gSignal = LED(6)
sclr = LED(5)

def clockPulse():
    clock.on()
    sleep(clockTime)
    clock.off()


def latchPulse():
    latch.on()
    sleep(clockTime)
    latch.off()

def init():
    data.off()
    latch.off()
    clock.off()
    gSignal.off()
    sclr.off()
    clockPulse()
    sclr.on()

def finalize():
    gSignal.on()
#    data.on()
#    sleep(clockTime)
#    clockPulse()
#    data.off()
    latchPulse()
    gSignal.off()
    clockPulse()

def sendBit(bit):
    if bit == 1:
        data.on()
    else:
        data.off()
    clockPulse()
    data.off()
    latchPulse()

def sendString(mystring):
    for val in mystring:
        sendBit(int(val))

init()
sendString("00000000")
finalize()

while True:
    mystring = input("Enter a string of 0s and 1s to display: ")
    sendString(mystring)
    finalize()
