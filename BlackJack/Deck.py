from random import choice
from Card import Card


class Deck():

    __ranks = list(range(2, 11)) + list("JQKA")
    __suits = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self, card=Card, ranks=__ranks, suits=__suits):

        self.__ranks = ranks
        self.__suits = suits
        self.__cards = [card(r, s)  for r in self.__ranks
                                    for s in self.__suits]
        self.__size = len(ranks) * len(suits)

    def __len__(self):
        return len(self.__cards)

    def __setitem__(self, position, value):
        self.__cards[position] = value

    def __getitem__(self, position):
        return self.__cards[position]

    def shuffle(self):

        free_positions = {pos for pos in range(len(self))}
        for card in self.__cards.copy():
            position = choice(list(free_positions))
            free_positions.remove(position)
            self[position] = card

    def get_random_card(self):
        return choice(self)

    def deal(self):
        return self.__cards.pop()

# my_deck = Deck()
# print(my_deck[0:20])
# my_deck.shuffle()
# print()
# print()
# print(my_deck[0:20])

