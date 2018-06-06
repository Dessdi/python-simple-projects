# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

import random

rangeMin = int(input("range: min "))
rangeMax = int(input("range: max "))
counter = 0
print("select number and I try to guess! ")

while True:
    guess = random.randint(rangeMin, rangeMax)
    print("is this your number? " + str(guess))
    counter = counter + 1
    result = input("correct/too low/to high ")

    if result == "correct":
        print("your number is " + str(guess) + " guess counter " + str(counter))
        break
    elif result == "too low":
        rangeMin = guess + 1
    elif result == "too high":
        rangeMax = guess - 1
    else:
        print("incorrect value")