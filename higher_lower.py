import os

from art import logo_higher_lower, logo_vs
from game_data_higher_lower import data
import random



def format_data(account):
    """"Formata os dados para exibição."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """ Checa a quantidade de seguidores """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# arte
print(logo_higher_lower)
score = 0
game_continue = True
# gerando um dado aleatorio para a pergunta B
account_b = random.choice(data)


while game_continue:

    # quem está na posi B vai ficar na A no próx round
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(logo_vs)
    print(f"Against B: {format_data(account_b)}.")

    # fazer a pergunta - quem tem mais seguidores ?
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    # checa a resposta ifs
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # limpa a tela entre os rounds
    os.system('clear')
    # arte
    print(logo_higher_lower)

    # respondendo e incrementando o score  - certo ou errado
    if is_correct:
        score += 1
        print(f"You're right! score: {score}")
    else:
        game_continue = False
        print(f"That's wrong! Final score: {score}")
