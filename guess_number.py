from random import randint
from art import logo_guessing_number

EASY_LEVEL = 10
HARD_LEVEL = 5


# função q checa se o num está perto ou longe
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# função que seta a dificuldade
def set_difficulty():
    level = input("Choose a difficulty. Type easy or hard? ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(logo_guessing_number)
    # escolhendo um num aleatório entre 1 e 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    # escolhendo a dificuldade
    turns = set_difficulty()

    # loop enquanto errar e ainda tiver chance
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # user insere um num  e chama a func pra saber se ta certo
        guess = int(input("Make a guess: "))
        # reduzindo o num de tentativas
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again..")


game()
