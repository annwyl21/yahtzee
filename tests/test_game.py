import pytest
from game import Play_game
from scoreboard import Scoreboard

# Look up and ask mentor about how to use 'mock' in tests to 'mock' run the game

def test_validate_dice_roll():
    test_game = Play_game()
    dice_roll = "5,4,3,2,1"
    results = test_game.validate_dice_roll_input(dice_roll)
    assert results == [5, 4, 3, 2, 1], "dice roll validation not working"

def test_user_dice_entry_error_acceptable():
    test_game = Play_game()
    compacted_entry = "65432"
    results = test_game.validate_dice_roll_input(compacted_entry)
    assert results == None, "compacted roll failed"

def test_user_entry_acceptable_spaces():
    test_game = Play_game()
    spaced_entry = "5 4 6 1 3"
    results = test_game.validate_dice_roll_input(spaced_entry)
    assert results == None, "spaced dice roll failed"

def test_injection():
    test_game = Play_game()
    injection = 'break'
    results = test_game.validate_dice_roll_input(injection)
    assert results == None, "failed to prevent injection"

def test_choose_score_computer():
    test_game = Play_game()
    results_dict = {'aces': 1, 'twos': 2, 'threes': 0, 'fours': 4, 'fives': 0, 'sixes': 6, 'three_of_a_kind': 0, 'four_of_a_kind': 0, 'full_house': 0, 'sm_straight': 0, 'lg_straight': 0, 'chance': 13, 'yahtzee': 0}
    results = test_game.choose_score('computer', results_dict)
    assert results == (('aces', 1)), "computer did not choose the first available entry on the blank scoreboard"

def test_choose_score_from_multiple_scores():
    test_game = Play_game()
    results_dict = {'aces': 2, 'twos': 2, 'threes': 0, 'fours': 4, 'fives': 0, 'sixes': 6, 'three_of_a_kind': 0, 'four_of_a_kind': 0, 'full_house': 0, 'sm_straight': 0, 'lg_straight': 0, 'chance': 13, 'yahtzee': 0}
    results = test_game.choose_score('computer', results_dict)
    assert results == (('aces', 2)), "computer did not choose the lowest score"





