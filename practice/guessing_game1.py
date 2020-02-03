# Q9: Guessing Game One
import random

print("Guessing Game 1\n")
play = True

while play:
    print("Computer Generating a Random Number...")
    comp_play = random.randint(1, 9)
    man_play = int(input("Guess the generated number(1 - 9): "))
    if comp_play == man_play:
        print("Guessed it right!!!")
    else:
        print("Got it wrong! It was %d" % comp_play)

    if str(input("Do you want to restart, yes or no? \n")) != "yes":
        play = False