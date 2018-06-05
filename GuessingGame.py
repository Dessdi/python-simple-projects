# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

rangeMin = int(input("range: min "))
rangeMax = int(input("range: max "))

randomNumber = random.randint(rangeMin, rangeMax)
userNumber = input("guess number: ")

while userNumber != "exit":

    if int(userNumber) == randomNumber:
        print("correct!")
        break
    elif int(userNumber) > randomNumber:
        print("too high")
        userNumber = input("guess number: ")
    elif int(userNumber) < randomNumber:
        print("too low")
        userNumber = input("guess number: ")