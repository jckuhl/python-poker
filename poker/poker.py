"""Poker API
An API for designing poker games, using the cards API.

Author:  Jonathan Kuhl
Created: December 29 2017

This API is considered open source freeware

https://github.com/jckuhl
"""

from cards import *
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class FiveCardPokerHand(Hand):
    """Creates a hand of cards for Five Card Stud
    Generates a score for the hand as well
    """

    value = None

    def __init__(self):
        super().__init__(size=5)
        # TODO: add scoring function upon initialization, value = score

    def score_hand(self):
        return self.value


class FiftyTwoDeck(Deck):
    """
    A standard 52 card deck, without Jokers.
    Cards are generated in order, use random.choice or random.sample
    to generate random hands
    """
    def __init__(self):
        super().__init__(size=52)
        card_suit = 1
        card_value = 2
        while len(self.deck_cards) < self.deck_size:
            self.deck_cards.append(Card(suit=card_suit, value=card_value))
            card_value += 1
            if card_value > 14:
                card_suit += 1
                card_value = 2


class Player:

    def __init__(self, money, hand):
        self.money = money
        self.hand = hand

    def raise_turn(self):
        # TODO: Implementation for raising a bid
        pass

    def call_turn(self):
        # TODO: Implementation for calling
        pass

    def pass_turn(self):
        # TODO: Implementation for passing/folding
        pass

    def bid(self, bet):
        # TODO: Implementation for making the initial bet
        pass

    def ante(self, amt, game):
        # TODO: Take money from player, put in game money
        # TODO: Determine which object handles game money
        self.money -= amt
        game.pot += amt

    def player_score(self):
        return self.hand.score_hand()


class FiveCardStud:

    def __init__(self):
        five_card_stud1 = FiveCardPokerHand()
        five_card_stud2 = FiveCardPokerHand()
        fifty_two = FiftyTwoDeck()
        player = Player(1000, five_card_stud1)
        player.hand.create_hand(fifty_two)
        clear()
        print("It's $50 to play, you have {} dollars".format(player.money))
        print("Here is your hand!")
        player.hand.show_hand()


class GameApp:

    def __init__(self, players, game_type):
        self.players = players
        self.game_type = game_type

    def game_loop(self):
        self.game_type()


if __name__ == "__main__":
    print("Welcome to Poker!")
    game = input("Press Enter to play or enter quit to quit\n").lower()
    if game != "quit":
        poker = GameApp(2, FiveCardStud)
        poker.game_loop()
