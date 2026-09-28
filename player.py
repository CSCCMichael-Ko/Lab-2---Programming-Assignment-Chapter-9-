"""
Program Name: player.py
Name (Author): Michael Ko
Purpose: This class represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss.
Date: 09/26/2026
"""

from coin import Coin

class Player:
    """
    This class represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss.
    """

    def __init__(self, name):
        """The initializer method. It should take a name as an argument and set up all three private attributes."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin() 

    def toss_coin(self):
        """ This method tells the player's coin to toss itself (e.g., self.__coin.toss())."""
        self.__coin.toss()

    def get_coin_side(self):
        """This method gets the side of the player's coin by calling the coin's get_sideup() method and returning its value."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Adds 1 to the __wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Subtracts 1 from the __wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the number of coins in the player's wallet."""
        return self.__wallet

    def get_name(self):
        """Returns the value of __name."""
        return self.__name