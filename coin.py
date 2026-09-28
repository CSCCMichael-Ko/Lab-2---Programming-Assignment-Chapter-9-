"""
Program Name: coin.py
Name (Author): Michael Ko
Purpose: This class represents a single, tossable coin. It only knows about its own state (heads or tails).
Starter Code: N/A. 
Date: 09/27/2026
"""

import random

class Coin:
    """
    This class represents a single, tossable coin. It only knows about its own state (heads or tails).
    """
    def __init__(self):
        "The initializer method that sets up the __sideup attribute."
        self.__sideup = "Heads"  

    def toss(self):
        """Generates a random number (0 or 1) and sets __sideup to 'Heads' or 'Tails' accordingly."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Returns the current value of __sideup."""
        return self.__sideup