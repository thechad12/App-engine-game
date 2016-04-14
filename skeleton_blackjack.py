import math
import random

def hand():
    card_1 = random.randint(1,11)
    card_2 = random.randint(1,11)
    if card_1 == 1 or card_2 == 1:
        card_1 = "Ace"
        card_2 = "Ace"
    hand = [card_1, card_2]
    return hand

def response():
    call = input("Hit or stay?")
    while call:
        if call == "hit":
            while call == "hit":
                new_card = random.randint(1,11)
                hand.append(new_card)
                return new_card
        elif call == "stay":
            break
            b = sum(hand)
            return b
            if b > 21:
                return "You lose"
            if b == 21:
                return "You win"
            if b < 21:
                return "Close"
