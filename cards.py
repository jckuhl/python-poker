import logging
import random
from enum import Enum

# Generic API for any card game

logging.basicConfig(filename="poker.log", filemode="w", level=logging.DEBUG)


class Suit(Enum):
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"


class Face(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Card:

    def __init__(self, suit, value):
        """
        __init__ for Card class
        :param suit:
        :param value:
        """
        self.suit = suit
        self.value = value
        if self.suit == 1:
            self.suit = Suit.HEARTS
        elif self.suit == 2:
            self.suit = Suit.CLUBS
        elif self.suit == 3:
            self.suit = Suit.DIAMONDS
        else:
            self.suit = Suit.SPADES

    def show_card(self):
        print(str(self))

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.value + other

    def __eq__(self, other):
        return self.value == other and self.suit.value == other

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def __ge__(self, other):
        return self.value > other or self.value == other

    def __le__(self, other):
        return self.value < other or self.value == other

    def __str__(self):
        if self.value <= 10:
            value = self.value
        else:
            if self.value == 11:
                value = "Jack"
            elif self.value == 12:
                value = "Queen"
            elif self.value == 13:
                value = "King"
            else:
                value = "Ace"
        return "|{} of {}|".format(value, self.suit.value)

    def __int__(self):
        """
        Returns the value of the card in the format 1002
        Where the 1000's place is the suit (1000-4000)
        And the number is the face value of the card
        So 1002 would be the Deuce of Hearts
        4014 would be the Ace of Spades
        :return:
        """
        if self.suit == Suit.HEARTS:
            return self.value + 1000
        elif self.suit == Suit.CLUBS:
            return self.value + 2000
        elif self.suit == Suit.DIAMONDS:
            return self.value + 3000
        else:
            return self.value + 4000

    def __iter__(self):
        pass
    

class Deck:

    """
    Class for a deck of cards
    Kept generic, so it can be a standard 52 card deck
    Or a Pinochle deck
    Or whatever else you want.
    """

    def __init__(self, size):
        self.deck_size = size
        self.deck_cards = []

    def remove_card(self, card):
        self.deck_cards.remove(card)

    def get_deck(self):
        return self.deck_cards

    def show_deck(self):
        deck_str = ""
        for card in self.deck_cards:
            deck_str += str(card)
        print(deck_str)

    def log_deck(self):
        """
        LOGGING METHOD
        REMOVE BEFORE DEPLOYMENT
        :return:
        """
        logging.info("Deck cards: {}".format(len(self.deck_cards)))
        hearts = clubs = diamonds = spades = 0
        for card in self.deck_cards:
            if card.suit == Suit.HEARTS:
                hearts += 1
            elif card.suit == Suit.CLUBS:
                clubs += 1
            elif card.suit == Suit.DIAMONDS:
                diamonds += 1
            else:
                spades += 1
            logging.info("{} |".format(card))
        logging.info("Hearts: {}, Clubs: {}, Diamonds: {}, Spades: {}".format(hearts, clubs, diamonds, spades))
        logging.info("*"*20)


class Hand:

    def __init__(self, size=2):
        self.size = size
        self.cards = []

    def get_hand(self):
        return self.cards

    def create_hand(self, deck):
        """
        Creates a hand of cards of size self.size.
        If self.size is greater than the number of cards in the deck,
        it just takes the remaining cards in the deck.

        Thanks to /u/Zigity_Zagity from r/learnpython
        :param deck:  takes a Deck() object
        :return: self.cards
        """
        try:
            self.cards = random.sample(deck.deck_cards, k=self.size)
        except ValueError:
            self.cards = random.sample(deck.deck_cards, k=len(deck.deck_cards))
        deck.deck_cards = [card for card in deck.deck_cards if card not in self.cards]
        deck.log_deck()
        return self.cards

    def show_hand(self):
        hand_str = ""
        for card in self.cards:
            hand_str += str(card)
        print(hand_str)

    def remove_card(self, card):
        self.cards.remove(card)

    def draw_card(self, deck):
        card = random.sample(deck.deck_cards, k=1)
        self.cards.append(card[0])
