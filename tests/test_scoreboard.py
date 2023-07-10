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
    results =Scoreboard(create_player).add_score((('threes', 3), False))
    assert results == {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}

def test_register_yahtzee_bonus():
    a_test = Scoreboard("A_Test")
    results = a_test.add_score((('aces', 5), True))
    assert results == {'aces': 5, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": ['X']}
    
def test_add_yahtzee_bonus():
    results =Scoreboard(create_player).add_score((('yahtzee', 50), True))
    assert results == {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': 50, "yahtzee_bonus_rolls": ['X']}

def test_dont_add_score():
    mr_test = Scoreboard("Mr Test")
    mr_test.add_score((('threes', 3), False))
    results = mr_test.add_score((('threes', 9), False))
    assert results == {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None, "yahtzee_bonus_rolls": []}

def test_apply_bonus():
    miss_test = Scoreboard("Miss Test")
    miss_test.add_score((('aces', 5), True))
    miss_test.add_score((('twos', 10), True))
    miss_test.add_score((('threes', 15), True))
    miss_test.add_score((('fours', 20), True))
    miss_test.add_score((('fives', 25), True))
    miss_test.add_score((('sixes', 30), True))
    results = miss_test.apply_bonus()
    assert results == {"upper_bonus": 35, "yahtzee_bonus": 300}

def test_dont_apply_bonus():
    mstr_test = Scoreboard("Mstr Test")
    mstr_test.add_score((('aces', 1), False))
    mstr_test.add_score((('twos', 2), False))
    mstr_test.add_score((('threes', 3), False))
    mstr_test.add_score((('fours', 4), False))
    mstr_test.add_score((('fives', 5), False))
    mstr_test.add_score((('sixes', 0), False)) 
    results = mstr_test.apply_bonus()
    assert results == {"upper_bonus": 0, "yahtzee_bonus": 0}
    
def test_apply_yahtzee_bonus():
    a_test = Scoreboard("Abi Test")
    a_test.add_score((('yahtzee', 50), True))
    a_test.add_score((('aces', 1), False))
    a_test.add_score((('twos', 2), False))
    a_test.add_score((('threes', 3), False))
    a_test.add_score((('fours', 4), False))
    a_test.add_score((('fives', 5), False))
    a_test.add_score((('sixes', 0), False))
    a_test.add_score((('three_of_a_kind', 0), False))
    a_test.add_score((('four_of_a_kind', 0), False))
    a_test.add_score((('full_house', 0), False))
    a_test.add_score((('sm_straight', 0), False))
    a_test.add_score((('lg_straight', 0), False))
    a_test.add_score((('chance', 0), False))
    results = a_test.apply_bonus()
    assert results == {"upper_bonus": 0, "yahtzee_bonus": 100}
# Adding results of an assumed game because the method apply_bonus will only be called at the end of a game when all the 'None' values have been replaced with ints

def test_grand_total():
    g_test = Scoreboard("Granny Test")
    g_test.add_score((('yahtzee', 50), True))
    g_test.add_score((('aces', 1), False))
    g_test.add_score((('twos', 2), False))
    g_test.add_score((('threes', 3), False))
    g_test.add_score((('fours', 4), False))
    g_test.add_score((('fives', 5), False))
    g_test.add_score((('sixes', 6), False))
    g_test.add_score((('three_of_a_kind', 3), False))
    g_test.add_score((('four_of_a_kind', 4), False))
    g_test.add_score((('full_house', 7), False))
    g_test.add_score((('sm_straight', 15), False))
    g_test.add_score((('lg_straight', 20), False))
    g_test.add_score((('chance', 10), False))
    g_test.apply_bonus()
    results = g_test.grand_total()
    assert results == 230
# Granny takes 13 turns, adds her scores, at the end of the game the bonus is applied and the grand total is calculated.
