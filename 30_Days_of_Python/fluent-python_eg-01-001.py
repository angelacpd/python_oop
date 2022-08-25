"""
A Pythonic Card Deck

Playing with dunder methods and namedtuple

Extended from book:
Fluent Python
Example 1-1
"""

import collections

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
        

if __name__ == "__main__":
    deck = FrenchDeck()
    print(f"length: {len(deck)}")
    for card in range(0, len(deck)):
        print(f"position {card}: {deck[card]}")

# Output
# length: 52
# position 0: Card(rank='2', suit='spades')
# position 1: Card(rank='3', suit='spades')
# position 2: Card(rank='4', suit='spades')
# position 3: Card(rank='5', suit='spades')
# position 4: Card(rank='6', suit='spades')
# position 5: Card(rank='7', suit='spades')
# position 6: Card(rank='8', suit='spades')
# position 7: Card(rank='9', suit='spades')
# position 8: Card(rank='10', suit='spades')
# position 9: Card(rank='J', suit='spades')
# position 10: Card(rank='Q', suit='spades')
# position 11: Card(rank='K', suit='spades')
# position 12: Card(rank='A', suit='spades')
# position 13: Card(rank='2', suit='diamonds')
# position 14: Card(rank='3', suit='diamonds')
# position 15: Card(rank='4', suit='diamonds')
# position 16: Card(rank='5', suit='diamonds')
# position 17: Card(rank='6', suit='diamonds')
# position 18: Card(rank='7', suit='diamonds')
# position 19: Card(rank='8', suit='diamonds')
# position 20: Card(rank='9', suit='diamonds')
# position 21: Card(rank='10', suit='diamonds')
# position 22: Card(rank='J', suit='diamonds')
# position 23: Card(rank='Q', suit='diamonds')
# position 24: Card(rank='K', suit='diamonds')
# position 25: Card(rank='A', suit='diamonds')
# position 26: Card(rank='2', suit='clubs')
# position 27: Card(rank='3', suit='clubs')
# position 28: Card(rank='4', suit='clubs')
# position 29: Card(rank='5', suit='clubs')
# position 30: Card(rank='6', suit='clubs')
# position 31: Card(rank='7', suit='clubs')
# position 32: Card(rank='8', suit='clubs')
# position 33: Card(rank='9', suit='clubs')
# position 34: Card(rank='10', suit='clubs')
# position 35: Card(rank='J', suit='clubs')
# position 36: Card(rank='Q', suit='clubs')
# position 37: Card(rank='K', suit='clubs')
# position 38: Card(rank='A', suit='clubs')
# position 39: Card(rank='2', suit='hearts')
# position 40: Card(rank='3', suit='hearts')
# position 41: Card(rank='4', suit='hearts')
# position 42: Card(rank='5', suit='hearts')
# position 43: Card(rank='6', suit='hearts')
# position 44: Card(rank='7', suit='hearts')
# position 45: Card(rank='8', suit='hearts')
# position 46: Card(rank='9', suit='hearts')
# position 47: Card(rank='10', suit='hearts')
# position 48: Card(rank='J', suit='hearts')
# position 49: Card(rank='Q', suit='hearts')
# position 50: Card(rank='K', suit='hearts')
# position 51: Card(rank='A', suit='hearts')
