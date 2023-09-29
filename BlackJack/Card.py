from collections import namedtuple

# Card = namedtuple("Card", ["rank", "suit"])

# print(Card.__mro__)

# card1 = Card(4, "spades")

# print(card1)

class Card(namedtuple("Card", ["rank", "suit"])):
  
  _symbol_to_number = {
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
  }

  _suit_to_unicode = {
    'spades': '♠', 
    'diamonds': '♦',
    'clubs': '♣',
    'hearts': '♥'
  }

  def __int__(self):
    return self.rank if isinstance(self.rank, int) else self._symbol_to_number[self.rank]

  def __str__(self):
    return f'{self.rank}{self._suit_to_unicode[self.suit]}'

  def __add__(self, other):
    return int(self) + int(other)
  
  def __radd__(self, other):
    return self.__add__(other)

# card1 = Card(4, "spades")
# card2 = Card("K", "spades")
# print(card1)
# print(int(card1))   # --> 4
# print(int(card2))   # --> 13

# print(card1 + card2)
# print(card2 + 5)    
# print(5 + card2)    



