import pytest
from game import Play_game

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


    