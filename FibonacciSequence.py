def getElementValue(element):
    if element==0:
        return 0
    elif element==1:
        return 1
    else:
        return getElementValue(element-1) + getElementValue(element-2)

number = input('enter a number ')

for i in range(int(number)):
    value = getElementValue(int(i))
    print(value)
