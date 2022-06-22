from gpiozero import LED
from time import sleep
from string import ascii_uppercase
import sys
import random
from base64 import decode

led = LED(22)
DIT_LENGTH = .5
DAH_LENGTH = 1
BETWEEN_LETTER = .1
PAUSE_LENGTH = 1
LETTERS_PER_ROUND = 5

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
    for _ in range(LETTERS_PER_ROUND):
        print("Get ready for the next sequence")
        sleep(2)
        mystring = "".join([random.choice(ascii_uppercase) for _ in range(stringLength)])
        for letter in mystring:
            play_letter(letter)
        guess = input("What letter(s) were just played? ")
        if guess.upper() == mystring:
            score += 1
            print("Correct! You now have " + str(score) + " points")
        else:
            print("Sorry, that is incorrect, it was atually " + mystring)
    return score

def evalScore(roundNumber, currentScore):
    code = random.randint(10000,99999)
    if LETTERS_PER_ROUND == currentScore:
        random.seed(roundNumber * 42)
        print(str(decode(b'WW91IGdvdCBhIHBlcmZlY3Qgc2NvcmUgZm9yIHRoaXMgbGV2ZWwhIFlvdXIgZmxhZyBpcyBjeU1Uew==')) + code + "}")

print("Round 1")
evalScore(1,5)
print("round 2")
evalScore(2,10)
print("round 3")
evalScore(3,15)


score = 0
score = runRound("Round 1, single letters", 1, score)
evalScore(1, score)
choice = input("Would you like to advance to round 2 (y/n)?  ")
if choice != 'y':
    print("Quitting")
    sys.exit()
prevScore = score
score = runRound("Round 2, two letters", 2, score)
evalScore(1, score - prevScore)
choice = input("Would you like to advance to round 3 (y/n)?  ")
if choice != 'y':
    print("Quitting")
    sys.exit()
score = runRound("Round 3, three letters", 3, score)
evalScore(1, score - prevScore)
print("Your final score was " + str(score) + " points")
