from cards import *


class FiveCardPokerHand(Hand):
    value = None

    def __init__(self):
        super().__init__(size=5)

    def score_hand(self):
        return self.value


class FiftyTwoDeck(Deck):

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
        pass

    def call_turn(self):
        pass

    def pass_turn(self):
        pass

    def bid(self, bet):
        pass

    def player_score(self):
        return self.hand.score_hand()


def game_loop():
    five_card_stud1 = FiveCardPokerHand()
    five_card_stud2 = FiveCardPokerHand()
    fifty_two = FiftyTwoDeck()
    player = Player(1000, five_card_stud1)
    player.hand.create_hand(fifty_two)
    player.hand.show_hand()

if __name__ == "__main__":
    game_loop()
