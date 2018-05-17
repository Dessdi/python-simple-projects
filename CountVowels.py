vowels = ['a', 'e', 'i', 'o', 'u']

text = input("count vowels in word: ")
number = 0

for sign in text:
    if sign in vowels:
        number = number + 1

print("number of vowels: ", number)
