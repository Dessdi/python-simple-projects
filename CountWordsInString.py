path = input("set file path")

with open(path) as file:
    words = file.read().split()
    print(len(words))
