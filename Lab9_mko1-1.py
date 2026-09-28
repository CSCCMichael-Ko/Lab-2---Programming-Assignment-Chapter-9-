"""
Program Name: Lab9_mko1-1.py
Name (Author): Michael Ko
Purpose: This file runs the game. It creates the Player objects and manages the game loop and rules.
Starter Code: N/A. 
Date: 09/27/2026
"""

from player import Player

def main():
    print("--- Coin Match Game ---")
    print("Welcome to the Coin Toss Game!")
    print("Each player starts with 20 coins.")
    print("Match = Player 1 wins the round")
    print("No match = Player 2 wins the round\n")

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    choice = input("Play a round? (y/n to continue): ")

    while choice.lower() == 'y':
        """Each player tosses their coin"""
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"\nPlayer 1 tossed {side1}")
        print(f"Player 2 tossed {side2}")

        """Determines winner"""
        if side1 == side2:
            print("Sides match! Player 1 wins the round.")
            player1.win_coin()
            player2.lose_coin()
        else:
            print("Sides do NOT match! Player 2 wins the round.")
            player2.win_coin()
            player1.lose_coin()

        """Reports amount in wallet"""
        print(f"Player 1 now has {player1.get_wallet()} coins.")
        print(f"Player 2 now has {player2.get_wallet()} coins.\n")

        """Game over"""
        if player1.get_wallet() == 0:
            print("Player 1 has run out of coins! Game Over.")
            break
        if player2.get_wallet() == 0:
            print("Player 2 has run out of coins! Game Over.")
            break

        choice = input("Play another round? (y/n to continue): ")

    """Final results"""
    print("\nFinal Results:")
    print(f"Player 1: {player1.get_wallet()} coins")
    print(f"Player 2: {player2.get_wallet()} coins")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()