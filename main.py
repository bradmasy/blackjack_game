from blackjack_classes import Player, Dealer
import blackjack_functions


def main():
    """ Drives the program."""
    while True:
        try:
            player_information = blackjack_functions.welcome_to_the_game()
            break
        except ValueError as message:
            print(message)
    player_one = blackjack_functions.initialize_player(player_information)
    card_deck = blackjack_functions.create_card_deck()
    dealer = Dealer(card_deck)
    player_hand = dealer.deal_hand()
    player_one.hand(player_hand)
    print(player_one._hand)

if __name__ == "__main__":
    main()
