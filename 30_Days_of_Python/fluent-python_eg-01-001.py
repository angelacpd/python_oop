"""
A Pythonic Card Deck

Playing with dunder methods and namedtuple

Extended from book:
Fluent Python
Example 1-1
"""

import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
    

if __name__ == "__main__":
    deck = FrenchDeck()
    
    print(f"length: {len(deck)}\n")
    
    for card in range(0, 3):
        print(f"position {card}: {deck[card]}")
    
    for rank, suit in deck:
        print(f"{rank} of {suit}")
    
    print(f"\nlast position: {deck[-1]}")
    
    print(f"\nrandom card: {choice(deck)}")
    
    print(f"\nslice deck:\nTop three cards: {deck[:3]}\nAces: {deck[12::13]}")
    
    print(f"\nin operator: {Card('A', 'diamonds') in deck}")
    
    for card in reversed(deck):
        print(card)
    
    for card in sorted(deck, key=spades_high):
        print(card)
    
    
# Output

# length: 52

# position 0: Card(rank='2', suit='spades')
# position 1: Card(rank='3', suit='spades')
# position 2: Card(rank='4', suit='spades')
# 2 of spades
# 3 of spades
# 4 of spades
# 5 of spades
# 6 of spades
# 7 of spades
# 8 of spades
# 9 of spades
# 10 of spades
# J of spades
# Q of spades
# K of spades
# A of spades
# 2 of diamonds
# 3 of diamonds
# 4 of diamonds
# 5 of diamonds
# 6 of diamonds
# 7 of diamonds
# 8 of diamonds
# 9 of diamonds
# 10 of diamonds
# J of diamonds
# Q of diamonds
# K of diamonds
# A of diamonds
# 2 of clubs
# 3 of clubs
# 4 of clubs
# 5 of clubs
# 6 of clubs
# 7 of clubs
# 8 of clubs
# 9 of clubs
# 10 of clubs
# J of clubs
# Q of clubs
# K of clubs
# A of clubs
# 2 of hearts
# 3 of hearts
# 4 of hearts
# 5 of hearts
# 6 of hearts
# 7 of hearts
# 8 of hearts
# 9 of hearts
# 10 of hearts
# J of hearts
# Q of hearts
# K of hearts
# A of hearts

# last position: Card(rank='A', suit='hearts')

# random card: Card(rank='J', suit='spades')

# slice deck:
# Top three cards: [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
# Aces: [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# in operator: True
