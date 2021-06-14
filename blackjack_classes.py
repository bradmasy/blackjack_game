import random


class Player:
    """ Represents a player in the game."""

    def __init__(self, name, bank_roll):
        self.name = name
        self.bank_roll = bank_roll
        self._hand = None

    def add_to_bank_roll(self, player_cash_to_bank):
        """Function allows a player to add money to they're bank roll."""
        self.bank_roll += player_cash_to_bank
        return self._bank_roll

    def hand(self, cards_list):
        self._hand = cards_list
        return self._hand


class Dealer:
    """ Represents a dealer in the game. """

    def __init__(self, card_deck):
        self._card_deck = card_deck

    def discard_card(self, card_value):
        """ Function simulates discarding a used card."""
        discard_pile = []
        index = self._card_deck.index(card_value)
        card = self._card_deck.pop(index)
        discard_pile.append(card)
        # TODO: maybe return the discard pile?

    def deal_hand(self):
        """ Function simulates the dealing of a hand to a player object.

        :return:
        """
        hand = []
        for i in range(2):
            random_card = random.choice(self._card_deck)
            hand.append(random_card)
            self.discard_card(random_card)
        return hand

    def print_drawn_cards(self):
        """ Print to the screen the hand drawn.

        :return:
        """

    @property
    def card_deck(self):
        return self._card_deck
