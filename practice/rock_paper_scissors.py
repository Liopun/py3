# Q8: ROCK PAPER SCISSORS

print("ROCK PAPER SCISSORS")

play = True
while play:
    print("Rock(r), Paper(p), Scissors(s)")
    p1 = str(input("**PLAYER 1** Enter the corresponding letter: ")).casefold()
    p2 = str(input("**PLAYER 2** Enter the corresponding letter: ")).casefold()

    play_dict = {'r': 1, 's': 2, 'p': 3}
    a = play_dict.get(p1)
    b = play_dict.get(p2)

    dif = a - b

    if dif in [-1, 2]:
        print("Player 1 wins!!")
    elif dif in [-2, 1]:
        print("Player 2 wins!!")
    else:
        print("It's a draw.")

    if str(input("Do you want to restart, yes or no? \n")) != "yes":
        play = False