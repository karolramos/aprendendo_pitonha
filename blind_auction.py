import os

from art import logo_blind_auction
print(logo_blind_auction)

bids = {}
bidding_finished = False


def clear():
    # os.system('cls')
    os.system('clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #   Exemplo: bidding_record = {"Anny": 80, "Matilda": 120} = O valor de Matilda será guardado como o maior
    for bidder in bidding_record:   # passando por cada CHAVE{nome}
        bid_amount = bidding_record[bidder]     # valor
        if bid_amount > highest_bid:    # comparando o valor acumulado com o novo valor
            highest_bid = bid_amount    # se o valor acumulado for maior, é armazenado na var
            winner = bidder     # setando o vencedor na var
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == 'no':
        find_highest_bidder(bids)
        bidding_finished = True
    elif should_continue == 'yes':
        clear()
    else:
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")

