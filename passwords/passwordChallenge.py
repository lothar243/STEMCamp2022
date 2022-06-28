#import lcd_i2c
from time import sleep
import string
import sys
import random
from base64 import b64decode

PASSWORDS_PER_ROUND = 3
TIME_TO_MEMORIZE = 20
TIME_AFTER_MEMORIZE = 15


def displayString(mystring, time):
    print(mystring)
    sleep(time)


def runRound(roundText, num_passwords, password_length, password_characters, score):
    print(roundText)
    for _ in range(PASSWORDS_PER_ROUND):
        print("Get ready for the next password, you have " + str(TIME_TO_MEMORIZE) + " seconds to memorize it")
        sleep(2)
        mystring = "".join([random.choice(password_characters) for _ in range(password_length)])
        displayString(mystring, TIME_TO_MEMORIZE)
        print("Ok, now you have to wait " + str(TIME_AFTER_MEMORIZE) + " more seconds before entering it.")
        sleep(TIME_AFTER_MEMORIZE)
        guess = input("What is the password? ")
        if guess == mystring:
            score += 1
            print("Correct!")
        else:
            print("Sorry, that is incorrect, it was atually " + mystring)
    return score

def evalScore(roundNumber, currentScore, password_length):
    code = str(random.randint(10000,99999))
    if PASSWORDS_PER_ROUND == currentScore:
        random.seed(roundNumber * PASSWORDS_PER_ROUND * password_length)
        print(str(b64decode(b'WW91IGdvdCBhIHBlcmZlY3Qgc2NvcmUgZm9yIHRoaXMgbGV2ZWwhIFlvdXIgZmxhZyBpcyBjeU1Uew=='))[2:-1] + code + "}")


# def runRound(roundText, num_passwords, password_length, password_characters):
score = 0
roundText = "Round 1, 6 characters, lower case only"
password_characters = string.ascii_lowercase
score = runRound(roundText, 3, 6, password_characters, score)
evalScore(1, score, 6)
choice = input("Would you like to advance to round 2 (y/n)?  ")
if choice != 'y':
    print("Quitting")
    sys.exit()
prevScore = score
roundText = "Round 2, 8 characters, lower and upper case with digits"
password_characters = string.string.ascii_uppercase + string.ascii_lowercase + string.digits
score = runRound(roundText, 3, 8, password_characters, score)
evalScore(1, score - prevScore, 8)
choice = input("Would you like to advance to round 3 (y/n)?  ")
if choice != 'y':
    print("Quitting")
    sys.exit()
roundText = "Round 3, 10 characters, lower and upper case with digits and special characters"
password_characters = string.string.ascii_uppercase + string.ascii_lowercase
score = runRound(roundText, 3, 10, password_characters, score)
evalScore(1, score - prevScore, 10)
print("Your final score was " + str(score) + " points")
