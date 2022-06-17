from gpiozero import LED
from time import sleep
from random import choice as random_choice
from string import ascii_uppercase
import sys

led = LED(22)
DIT_LENGTH = .5
DAH_LENGTH = 1
BETWEEN_LETTER = .1
PAUSE_LENGTH = 1

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def flash_light(time):
    led.on()
    sleep(time)
    led.off()
    sleep(BETWEEN_LETTER)

def play_letter(letter):
    sequence = MORSE_CODE_DICT[letter.upper()]
    for char in sequence:
        if char == ".":
            flash_light(DIT_LENGTH)
        elif char == "-":
            flash_light(DAH_LENGTH)
        else:
            print("Encountered unknown character: " + char)
    sleep(PAUSE_LENGTH)

def sample():
    for letter in "hello":
        play_letter(letter)

def runRound(roundText, stringLength, score):
    print(roundText)
    for _ in range(5):
        print("Get ready for the next sequence")
        sleep(2)
        mystring = "".join([random_choice(ascii_uppercase) for _ in range(stringLength)])
        for letter in mystring:
            play_letter(letter)
        guess = input("What letter(s) were just played? ")
        if guess.upper() == mystring:
            score += 1
            print("Correct! You now have " + str(score) + " points")
        else:
            print("Sorry, that is incorrect, it was atually " + mystring)
    return score

score = 0
score = runRound("Round 1, single letters", 1, score)
choice = input("Would you like to advance to round 2 (y/n)?  ")
if choice != 'y':
    print("Quitting")
    sys.exit()
score = runRound("Round 2, two letters", 2, score)
choice = input("Would you like to advance to round 3 (y/n)?  ")
if choice != 'y':
    print("Quitting")
    sys.exit()
score = runRound("Round 3, three letters", 3, score)
print("Your final score was " + str(score) + " points")
