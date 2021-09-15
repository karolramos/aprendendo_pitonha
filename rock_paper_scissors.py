import random
from art import logo_rock
from art import logo_paper
from art import logo_scissors


game_images = [logo_rock, logo_paper, logo_scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n ").lower())
print(game_images[user_choice])  # imagem compatível com o num escolhido

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])  # imagem compatível com o num escolhido

if user_choice >= 3 or user_choice < 0:
	print("You typed an invalid number, you lose! ")
elif user_choice == 0 and computer_choice == 2:
	print("You win!")
elif computer_choice > user_choice:
	print("You lose!")
elif user_choice > computer_choice:
	print("You win!")
elif computer_choice == 0 and user_choice == 2:
	print("You lose!")
elif computer_choice == user_choice:
	print("It's a draw!")
