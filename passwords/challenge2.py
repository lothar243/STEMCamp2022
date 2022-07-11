#import lcd_i2c
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


with open("diceware.txt", 'r') as dicewareFile:
    # wordlist = [line.split(" ")[1] for line in dicewareFile.readlines()]
    wordlist = []
    lines = dicewareFile.readlines()
    for line in lines:
        words = line.split()
        word = words[1]
        wordlist.append(word.capitalize())


def runRound(roundText, num_passwords, password_length, password_characters, score):
    print(roundText)
    for _ in range(PASSWORDS_PER_ROUND):
        print("Here's your password. Press enter when you've memorized it")
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


startingLevel = int(input("Which level would you like to do? (1-3) "))
score = 0
if startingLevel == 1:
    roundText = "Round 1, 3 words, search space = 7776^3 = 470184984576 = 4e11"
    score = runRound(roundText, 3, 3, wordlist, score)
    evalScore(1, score)
    prevScore = score
elif startingLevel == 2:
    roundText = "Round 2, 4 words, search space = 7776^4 = 3656158440062976 = 3e15"
    password_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    score = runRound(roundText, 3, 4, wordlist, score)
    evalScore(2, score)
elif startingLevel == 3:
    roundText = "Round 3, 5 words, search space = 7776^5 = 28430288029929701376 = 2e19"
    password_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    score = runRound(roundText, 3, 5, wordlist, score)
    evalScore(3, score)
