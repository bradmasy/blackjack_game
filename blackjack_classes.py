class Player:
    def __init__(self, name,bank_roll,player_hand):
        self._name = name
        self._bank_roll = bank_roll
        self._player_hand = player_hand

        def bank_roll(player_cash_to_bank):
            """Function allows a player to add money to they're bank roll"""
            self._bank_roll += player_cash_to_bank
            return self._bank_roll


