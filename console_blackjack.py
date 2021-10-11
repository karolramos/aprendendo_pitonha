############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os

from mini_projects_python.art import logo_blackjack


def deal_card():
    """ retorna uma carta aleatória do baralho """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """ pega a lista de cartas e retorna o valor somado nelas """
    if sum(cards) == 21 and len(cards) == 2:  # checando blackjack
        return 0
# checando se tem 11 e se a pontuação está acima de 21, se tiver substitua 11 por 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(logo_blackjack)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # adicionando duas cartas para os dois(usuário e computador)
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)  # ou user_cards.append(deal_card()) da a mesma coisa
        computer_cards.append(deal_card())  # adc duas cartas para cada um.

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"You cards: {user_cards}, current score: {user_score} ")
        print(f"Computer cards: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            answer = input("Type 'y' to get another card, type 'n' to pass: ").islower()
            if answer == "y":
                user_cards.append(deal_card())  # se o user decidir continuar jogando vai chamar outras cartas
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)    # atualizando o score

    print(f" Your final hand: {user_cards}, final score: {user_score} ")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score} ")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()

