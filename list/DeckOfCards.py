# create a deck of cards
deck = [x for x in range(52)]

# create suits and ranks list
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
         "Queen", "King" 
        ]

import random

random.shuffle(deck)

# displa the first four cards
for i in range(4) :
    suit = suits[deck[i] // 13]
    rank =  ranks[deck[i] % 13]
    
    print("Card number", deck[i], "is the", rank, "of", suit)