import time

import numpy as np

np.random.seed(int(time.time()))

WINNING_STATUS = 63

def update_status(curr_status: int) -> int:
    """Update the player status after rolling the dice

    Parameters
    ----------
    curr_status : int
        Current status of the player, i.e. its position as an integer
        from 1 to 63 

    Returns
    -------
    int
        Updated status of the player after rolling the dice, i.e.
        the new player position as an integer from 1 to 63
    """
    dice_rolls = np.random.randint(low=1, high=6, size=2)
    new_status = curr_status + dice_rolls.sum()
    
    if new_status>WINNING_STATUS:
        new_status = 2*WINNING_STATUS-new_status # If exceeding max state, step back by difference
    
    return new_status

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
    players_status = [0] * players

    while True:
        for ith_player, _ in enumerate(players_status):
            new_status = update_status(players_status[ith_player])
            players_status[ith_player] = new_status

            if players_status[ith_player]== WINNING_STATUS:
                print(f"Player {ith_player+1} wins!")
                return ith_player + 1, players_status
            

if __name__ == "__main__":
    players=0
    while not correct_number_of_players(players):
        players = int(input("How many players are going to play? [2-6] "))

    start_game(players=players) 
