import numpy as np
import pytest
from src.game import start_game, WINNING_STATUS


def test_single_player_game_ends_with_victory():
    win_player, players = start_game(players=1)
    assert win_player == 1
    assert players[win_player - 1].status == WINNING_STATUS


@pytest.mark.parametrize("n_players", [2, 3, 4, 5, 6])
def test_multiplayers_game_ends_with_victory(n_players):
    seed = 27
    np.random.seed(seed)

    win_player, players = start_game(players=n_players)
    assert 1 <= win_player <= n_players
    assert all(
        player.status < WINNING_STATUS
        for player in players
        if player.id != win_player
    )
    assert players[win_player - 1].status == WINNING_STATUS
