##Generating random strings until a given string is generated

import string
import random
import time
from turtle import pos

possibleChar = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

t = input(str("Enter target text: "))

attemptThis = ''.join(random.choice(possibleChar) for i in range(len(t)))

attemptNext = ''
completed = False
itr = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True

    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleChar)
        else:
            attemptNext += t[i]
    
    itr += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched after " + str(itr) + " iterations")