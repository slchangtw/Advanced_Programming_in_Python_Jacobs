"""
File: cards.py

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit
   
    def __gt__(self, other):
        if type(self) != type(other):
            raiseTypeError('Type of {0} is not same as Type of {1}'.format(type(self), type(other)))
        
        if self.rank == 1 and other.rank != 1:
            return True
        if self.rank != 1 and other.rank == 1:
            return False
        if self.rank > other.rank:
            return True
        elif self.rank < other.rank:
            return False
        
        if self.rank == other.rank:
            return Card.SUITS.index(self.suit) < Card.SUITS.index(other.suit)
        
import random

class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self._cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self._cards.append(c)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self._cards)

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self._cards.pop(0)

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(self._cards)

    def __str__(self): 
        """Returns the string representation of a deck."""
        result = ''
        for c in self._cards:
            result = self.result + str(c) + '\n'
        return result

