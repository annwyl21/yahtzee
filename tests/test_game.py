import pytest
from game import Play_game

@pytest.fixture
def create_game():
	test_game = Play_game('test')

# Look up and ask mentor about how to use 'mock' in tests to 'mock' run the game

def test_validate_dice_roll():
    dice_roll = "5 4 3 2 1"
    results = Play_game(create_game).validate_dice_roll_input()
    assert results == [5 4 3 2 1], "dice roll validation not working"
