import pytest
from scoreboard import Scoreboard    # The code to test


# https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
@pytest.fixture
def create_player():
    mrs_test = Scoreboard("Mrs Test")

def test_get_scoreboard():
    results = Scoreboard(create_player).getscore_dict()
    assert results == {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}, "Scoreboard is incorrect"
    #if I call the scoreboard, the test returns an empty scoreboard

def test_add_score():
    results =Scoreboard(create_player).add_score(('threes', 3))
    assert results == {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}

def test_dont_add_score():
    mr_test = Scoreboard("Mr Test")
    mr_test.add_score(('threes', 3))
    results = mr_test.add_score(('threes', 9))
    assert results == {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}

def test_apply_bonus():
    miss_test = Scoreboard("Miss Test")
    miss_test.add_score(('aces', 6))
    miss_test.add_score(('twos', 12))
    miss_test.add_score(('threes', 18))
    miss_test.add_score(('fours', 24))
    miss_test.add_score(('fives', 30))
    miss_test.add_score(('sixes', 36))
    results = miss_test.apply_bonus()
    assert results == {"upper_bonus": 35, "yahtzee_bonus": 0}

def test_dont_apply_bonus():
    mstr_test = Scoreboard("Mstr Test")
    mstr_test.add_score(('aces', 1))
    mstr_test.add_score(('twos', 2))
    mstr_test.add_score(('threes', 3))
    mstr_test.add_score(('fours', 4))
    mstr_test.add_score(('fives', 5)) #Mrs Test has scored 15 points in the upper section
    results = mstr_test.apply_bonus()
    assert results == {"upper_bonus": 0, "yahtzee_bonus": 0}
