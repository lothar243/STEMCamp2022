from time import sleep
import string
import sys
from os import system
import random
from base64 import b64decode
import hashlib
from termios import tcflush, TCIOFLUSH

PASSWORDS_PER_ROUND = 3
TIME_TO_MEMORIZE = 20
TIME_AFTER_MEMORIZE = 15


with open(sys.argv[0], 'r') as thisfile:
    myhash = hashlib.md5(thisfile.read().encode()).hexdigest()
    inthash = int(myhash, 16)


def displayString(mystring, time):
    print(mystring)
    sleep(time)
    system('clear')


def runRound(roundText, num_passwords, password_length, password_characters, score):
    print(roundText)
    for _ in range(PASSWORDS_PER_ROUND):
        print("Here's the next password, press enter when you're done memorizing it")
        mystring = "".join([random.choice(password_characters) for _ in range(password_length)])
        print(mystring)
        input()
        system('clear')
        print("Ok, now you have to wait " + str(TIME_AFTER_MEMORIZE) + " more seconds before entering it.")
        sleep(TIME_AFTER_MEMORIZE)
        tcflush(sys.stdin, TCIOFLUSH)
        system('clear')
        guess = input("What is the password? ")
        if guess == mystring:
            score += 1
            print("Correct!")
        else:
            print("Sorry, that is incorrect, it was atually " + mystring)
    return score

def evalScore(roundNumber, currentScore):
    if PASSWORDS_PER_ROUND == currentScore:
        random.seed(roundNumber * inthash)
        code = str(random.randint(10000,99999))
        print(str(b64decode(b'WW91IGdvdCBhIHBlcmZlY3Qgc2NvcmUgZm9yIHRoaXMgbGV2ZWwhIFlvdXIgZmxhZyBpcyBjeU1Uew=='))[2:-1] + code + "}")


startingLevel = int(input("On which level would you like to do? (1-3) "))
score = 0
if startingLevel == 1:
    roundText = "Round 1, 8 characters, lower case only, search space: 26^8 = 208827064576 = 2e11"
    password_characters = string.ascii_lowercase
    score = runRound(roundText, 3, 8, password_characters, score)
    evalScore(1, score)
elif startingLevel == 2:
    roundText = "Round 2, 8 characters, lower and upper case with digits, search space: 62^8 = 218,340,105,584,896 = 2e14"
    password_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    score = runRound(roundText, 3, 8, password_characters, score)
    evalScore(2, score)
elif startingLevel == 3:
    roundText = "Round 3, 10 characters, lower and upper case with digits and special characters, search space 94^10 = 53,861,511,409,489,970,176 = 5e19"
    password_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    score = runRound(roundText, 3, 10, password_characters, score)
    evalScore(3, score)

