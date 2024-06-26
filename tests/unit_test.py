import numpy as np
import pytest

from src.game import correct_number_of_players, Player


def test_update_status():
    curr_status = 40
    exp_new_status = 45
    seed = 27
    np.random.seed(seed)
    player = Player(0, "Test player")
    player.status = curr_status

    player.update_status()

    assert player.status == exp_new_status


def test_update_status_above_63():
    curr_status = 60
    exp_new_status = 61
    seed = 27
    np.random.seed(seed)
    player = Player(0, "Test player")
    player.status = curr_status

    player.update_status()

    assert player.status == exp_new_status


@pytest.mark.parametrize("players", [1, 7, 10_000])
def test_check_players_number_return_false(players):
    assert correct_number_of_players(players) == False


@pytest.mark.parametrize("players", [2, 3, 4, 5, 6])
def test_check_players_number_return_true(players):
    assert correct_number_of_players(players) == True
