import pytest
from scoreboard import Scoreboard    # The code to test


# https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
@pytest.fixture
def create_player():
    mrs_test = Scoreboard("Mrs_Test")


def test_get_scoreboard():
    #mrs_test = Scoreboard("Mrs Test") # replaced by fixture
    results = Scoreboard(create_player).getscore_dict()
    assert results == {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}, "Scoreboard is incorrect"
    #if I call the scoreboard, the test returns an empty scoreboard

def test_add_score():
    results =Scoreboard(create_player).add_score(('threes', 3))
    assert results == {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}
    #if I add a score to the scoreboard, the test returns a scoreboard with that score added

# can I run the previous test and have the results impact in this instead of creating a new player?
def test_dont_add_score():
    mr_test = Scoreboard("Mr Test") # create a player
    mr_test.add_score(('threes', 3)) # add a score to the player's scoreboard
    results = Scoreboard(mr_test).add_score(('threes', 9)) # try to add a score to the player's scoreboard that already exists
    assert results == {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}
    #if I try to add a score to the scoreboard that already exists, the test returns a scoreboard with the original score still there

def test_apply_bonus():
    mr_test = Scoreboard("Mr Test")
    mr_test.add_score(('aces', 6))
    mr_test.add_score(('twos', 12))
    mr_test.add_score(('threes', 18))
    mr_test.add_score(('fours', 24))
    mr_test.add_score(('fives', 30))
    mr_test.add_score(('sixes', 36)) #Mr Test has scored 126 points in the upper section
    results = Scoreboard(mr_test).apply_bonus()
    assert results == {"upper_bonus": 35, "yahtzee_bonus": None}

def test_dont_apply_bonus():
    mr_test = Scoreboard("Mr Test")
    mr_test.add_score(('aces', 1))
    mr_test.add_score(('twos', 2))
    mr_test.add_score(('threes', 3))
    mr_test.add_score(('fours', 4))
    mr_test.add_score(('fives', 5)) #Mrs Test has scored 15 points in the upper section
    results = Scoreboard(mr_test).apply_bonus()
    assert results == {"upper_bonus": None, "yahtzee_bonus": None}

