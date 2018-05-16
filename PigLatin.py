vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    text = input('type something ')
    if (text == "exit"):
        break
    else:
        if(text[0].lower() in vowels):
            print(text + 'way')
        else:
            for i, char in enumerate(text):
                if(char in vowels):
                    index = i
                    break

            print(text[i:].lower() + text[:i].lower() + "ey")

