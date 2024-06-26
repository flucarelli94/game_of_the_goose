import time

import numpy as np

np.random.seed(int(time.time()))

WINNING_STATUS = 63

class Player:
    def __init__(self, id, name):
        self.id = id
        self.status = 0
        self.name = name
        self.in_hotel = False

    def update_status(self):
        """Update the player status after rolling the dice, i.e.
            the new player position as an integer from 1 to 63
        """
        dice_rolls = np.random.randint(low=1, high=6, size=2)
        new_status = self.status + dice_rolls.sum()

        new_status = check_jumping(new_status)
        
        if new_status>WINNING_STATUS:
            new_status = 2*WINNING_STATUS-new_status # If exceeding max state, step back by difference

        self.status = new_status
# def check_hotel(curr_status: int) -> 

def check_jumping(curr_status: int) -> int:
    if curr_status == 6:
        print("🌉 You're on the bridge, go to 12!")
        return 12
    if curr_status == 42:
        print("❤️‍🩹 You've fallen into the well, go to 39!")
        return 39
    if curr_status == 58:
        print("💀 You died, go back to the beginning!")
        return 1
    
    return curr_status

def correct_number_of_players(players: int) -> bool:
    return 2<=players<=6

def start_game(*, players: int = 0)-> tuple[int, list[int]]:
    """Launch the game

    Parameters
    ----------
    players : int
        Number of players. It must be a number between 2 and 6

    Returns
    -------
    tuple[int, list[int]]
        The index of the winning player and the list with the
        players status. The player index starts from 1
    """
    player_names =["Fra", "Robin", "Chiara", "Michele", "Bobby", "Fede"]
    players_list = [Player(i+1, player_names[i]) for i in range(players)]

    while True:
        for player in players_list:
            print(f"It's {player.name} turn")
            player.update_status()

            print(f"\tReached position {player.status}")

            if player.status == WINNING_STATUS:
                print(f"{player.name} wins!")
                return player.id, players_list
            

if __name__ == "__main__":
    players=0
    while not correct_number_of_players(players):
        players = int(input("How many players are going to play? [2-6] "))

    start_game(players=players) 

