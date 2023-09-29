from typing import Optional
from Card import Card
from Deck import Deck
from enum import Enum

class BlackJackCard(Card):
    
  _symbol_to_number = {
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,
  }

# card1 = BlackJackCard(4, "spades")
# card2 = BlackJackCard("K", "spades")

# print(card1 + card2)

class BlackJackHand():

  def __init__(self, cards: Optional[list[BlackJackCard]]=None ):

    if cards is None:
      self.__cards = []
    else:
      self.__cards: list[BlackJackCard] = cards

  def add_card(self, card):
    self.__cards.append(card)

  def show_cards(self):
    return " ".join(map(str, self.__cards)) 
  
  def get_score(self):

    score = sum(self.__cards)

    if score <= 21:
      return score

    # si sumando los 'A' como 11 que es su valor
    # por defecto nos pasamos, vamos restando de
    # de a uno hasta bajar de 21
    for c in self.__cards:
      if c.rank == 'A':
        score -= 10
        if score <= 21:
          return score
        
    return score
  

# Algoritmo principal

suits = ["spades", "diamonds", "clubs", "hearts"]*6     # Se juega con 6 masos mezclados
black_jack_deck = Deck(card=BlackJackCard, suits=suits)

player_cards = BlackJackHand()
house_cards = BlackJackHand()

black_jack_deck.shuffle()

player_cards.add_card(black_jack_deck.deal())
player_cards.add_card(black_jack_deck.deal())
house_cards.add_card(black_jack_deck.deal())

print(f'Your cards: {player_cards.show_cards()}, current_score: {player_cards.get_score()}')
print(f'House cards: {house_cards.show_cards()}')
print()

class Match_result(Enum):
  PLAYER_WIN = 1
  HOUSE_WIN = 2
  DRAW = 3

result = None
player_decision = input("Write 'y' to get another card, or 'n' to pass: ")

while player_decision != 'n':
  if player_decision == 'y':
    player_cards.add_card(black_jack_deck.deal())
    print(f'Your cards: {player_cards.show_cards()}, current_score: {player_cards.get_score()}')
    print(f'House cards: {house_cards.show_cards()}')
    print()
    if player_cards.get_score() > 21:
      break
    player_decision = input("Write 'y' to get another card, or 'n' to pass: ")
  else:
    print('Invalid option')
    player_decision = input("Write 'y' to get another card, or 'n' to pass: ")

while not result:
  house_cards.add_card(black_jack_deck.deal())
  if house_cards.get_score() < 17:
    continue
  if house_cards.get_score() < player_cards.get_score() and player_cards.get_score() <= 21:
    continue
  if house_cards.get_score() == player_cards.get_score():
    result = Match_result.DRAW
  elif house_cards.get_score() <= 21:
    result = Match_result.HOUSE_WIN
  else:
    result = Match_result.PLAYER_WIN


print(f'Your cards: {player_cards.show_cards()}, current_score: {player_cards.get_score()}')
print(f'House cards: {house_cards.show_cards()}, current_score: {house_cards.get_score()}')
print(result)



