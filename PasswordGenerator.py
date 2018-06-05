# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random
import string

charList = string.ascii_lowercase

passwordLength = int(input("length: "))

upperCase = input("upper case? yes/no ")
if upperCase == "yes":
    charList = charList + string.ascii_uppercase

numbers = input("numbers? yes/no ")
if numbers == "yes":
    charList = charList + string.digits

special = input("special signs? yes/no ")
if special == "yes":
    charList = charList + string.punctuation

password = ''.join(random.choice(charList) for n in range(passwordLength))
print(password)

