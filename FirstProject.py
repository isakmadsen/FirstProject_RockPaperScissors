from random import randint

choices = ["Rock", "Paper", "Scissors"]

compchoice = choices[randint(0, 2)]

player = False

while not player:

    player = input("Rock Paper or Scissors?")
    if player == compchoice:
        print("Tie")
    elif player == "Rock":
        if compchoice == "Paper":
            print("You lose.", compchoice, "wins vs.", player)
        else:
            print("You win.", player, "wins vs.", compchoice)
    elif player == "Paper":
        if compchoice == "Scissors":
            print("You lose.", compchoice, "wins vs.", player)
        else:
            print("You win.", player, "wins vs", compchoice)
    elif player == "Scissors":
        if compchoice == "Rock":
            print("You lose.", compchoice, "wins vs.", player)
        else:
            print("You win.", player, "wins vs", compchoice)
    else:
        print("Wrong move mate")

        player == False
        compchoice == choices[randint(0, 2)]