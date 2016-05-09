import math
import random


card_1 = random.randint(1,11)
card_2 = random.randint(1,11)
if card_1 == 1 or card_2 == 1:
    card_1 = "Ace"
    card_2 = "Ace"
hand = [card_1, card_2]
print hand

call = input("Hit or stay?")
while hand < 21:
    if call == "hit":
        new_card = random.randint(1,11)
        hand.append(new_card)
        print new_card
    elif call == "stay":
        break
        b = sum(hand)
        print b
        if b > 21:
            print "You lose"
        if b == 21:
            print "You win"
        if b < 21:
            print "You were Close"
