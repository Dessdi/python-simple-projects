# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
while True:

    input1 = input("rock, paper or scissors? ").lower()
    input2 = input("rock, paper or scissors? ").lower()

    if input1 == input2:
        print("tie")
    elif input1 == "rock":
        if input2 == "paper":
            print("paper wins")
        elif input2 == "scissors":
            print("rock wins")
        else:
            print("wrong value")
    elif input1 == "paper":
        if input2 == "rock":
            print("paper wins")
        elif input2 == "scissors":
            print("scissors win")
        else:
            print("wrong value")
    elif input1 == "scissors":
        if input2 == "rock":
            print("rock wins")
        elif input2 == "paper":
            print("scissors win")
        else:
            print("wrong value")
    else:
        print("wrong value")

    endGame = input("want to start a new game? ")
    if endGame == "yes":
        continue
    else:
        break
