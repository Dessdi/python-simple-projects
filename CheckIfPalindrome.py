text = input("check if the word is palindrome: ")

if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")

