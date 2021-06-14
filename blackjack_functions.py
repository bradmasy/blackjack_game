from blackjack_classes import Player, Dealer
import re
import random

# initialize player
PLAYER_NAME_INDEX = 0
PLAYER_CASH_INDEX = 1

# display hand
PLAYER_CARD_ONE = 0
PLAYER_CARD_TWO = 1
PLAYER_CARD_SUITE_VALUE = 0
PLAYER_CARD_FACE_VALUE = 1

# ace value
BLACK_JACK = 21

def validate_bank_roll(bank_roll):
    """ Function uses regular expressions to validate bank roll.
    """
    expression = re.search(r"^[^0][0-9]*\.[0-9][0-9]", bank_roll)
    if expression:
        validation = True
    else:
        validation = False
    return validation


def welcome_to_the_game():
    """ Welcomes player to the game and gathers attributes needed to create the player from a Player class.
    """
    print("Lets play Blackjack!")
    player_name = input("whats your name? ")
    bank_roll = input("how much money would you like to put in your bank? ")
    if validate_bank_roll(bank_roll):
        player_information_list = [player_name, float(bank_roll)]
    else:
        raise ValueError("Incorrect Float")

    return player_information_list


def initialize_player(player_list):
    """ Initializes a player object and prints the players details.

    :param player_list: must be of list data type and contain a player name string and a float value representing the
    players initial bank roll
    :return: player object/instance
    """
    player = Player(player_list[PLAYER_NAME_INDEX], player_list[PLAYER_CASH_INDEX])
    print(f"Welcome to the game {player.name}, you have deposited {player.bank_roll:.2f}")
    return player


def shuffle_deck(card_deck):
    """ Simulates a shuffled card deck by randomizing the the card values and returning them in a new list.
    :param card_deck: must be of list data type and be composed of lists holding the card suite and card value
    :return: shuffled card deck
    """
    shuffled_deck = []
    i = 0
    while i < len(card_deck):
        random_card = random.choice(card_deck)
        shuffled_deck.append(random_card)
        i += 1
    return shuffled_deck


def create_card_deck():
    """ Creates a deck of cards, each card is represented by a list within a list.
    :return: card deck
    """
    card_deck = []
    card_value = ["ACE", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
    card_suite = ["DIAMONDS", "HEARTS", "SPADE", "CLUBS"]
    for value in card_value:
        for suite in card_suite:
            suite_and_value = [suite, value]
            card_deck.append(suite_and_value)
    shuffled_deck = shuffle_deck(card_deck)
    return shuffled_deck


def card_values():
    card_deck = ["ACE", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
    values = [[1, 11], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    associated_card_values = []
    for card in range(len(card_deck)):
        card_and_value = [values[card], card_deck[card]]
        associated_card_values.append(card_and_value)
    return associated_card_values

def ace_value(ace):
    #TODO: decision of ace value based on total value of hand
    if ace + second_card_value > BLACK_JACK:
        ace = 1
    else:
        ace = 11


def display_hand(hand):
    card_value = card_values()
    card_one_value = hand[PLAYER_CARD_ONE][PLAYER_CARD_FACE_VALUE]
    card_two_value = hand[PLAYER_CARD_TWO][PLAYER_CARD_FACE_VALUE]
    values = []
    print(card_one_value)
    for card_and_value in card_value:
        if card_one_value in card_and_value[1]:

            values.append(card_and_value[0])
        elif card_two_value in card_and_value[1]:
            values.append(card_and_value[0])
    print(values)
    #players_hand_value = sum(values)
    #print(players_hand_value)
    print(f"your cards are {hand[0]} and {hand[1]}")


display_hand([["DIAMONDS","ACE"], ["SPADE", "2"]])


def hit_stand_or_bust():
    decision = input("would you like to hit or stand? ")
    if decision == "hit":
        Dealer.deal_hand()
    elif decision == "stand":
        pass


def round():
    # TODO
    pass
