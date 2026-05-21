import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input(f"Choose [r]ock, [p]aper, or [s]cissors:\n")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again ...")

computer_random_number = random.randint(1, 3)

if computer_random_number == 1:
    computer_move = "Rock"
elif computer_random_number == 2:
    computer_move = "Paper"
else:
    computer_move = "Scissors"

if player_move == rock and computer_move == scissors or\
   player_move == paper and computer_move == rock     or \
   player_move == scissors and computer_move == paper:
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")
