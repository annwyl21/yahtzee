from scoreboard import Scoreboard    # The code to test
import unittest   # The test framework
#import pytest

# https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
# @pytest.fixture
# def name():
#     mrs_test = Scoreboard("Mrs_Test")

class Test_TestScoreboard(unittest.TestCase):
    def test_get_scoreboard(self):
        mrs_test = Scoreboard("Mrs Test")
        self.assertEqual(Scoreboard.getscore_dict(mrs_test), {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None})
        #if I call the scoreboard, the test returns an empty scoreboard

    def test_add_score(self):
        mrs_test = Scoreboard("Mrs Test")
        self.assertEqual(Scoreboard.add_score(mrs_test, ('threes', 3)), {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None})
        #if I add a score to the scoreboard, the test returns a scoreboard with that score added

    def test_dont_add_score(self):
        mrs_test = Scoreboard("Mrs Test")
        mrs_test.add_score(('threes', 3))
        self.assertEqual(Scoreboard.add_score(mrs_test, ('threes', 9)), {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None})
        #if I try to add a score to the scoreboard that already exists, the test returns a scoreboard with the original score still there
    
    def test_apply_bonus(self):
        mrs_test = Scoreboard("Mrs Test")
        mrs_test.add_score(('aces', 6))
        mrs_test.add_score(('twos', 12))
        mrs_test.add_score(('threes', 18))
        mrs_test.add_score(('fours', 24))
        mrs_test.add_score(('fives', 30))
        mrs_test.add_score(('sixes', 36)) #Mrs Test has scored 126 points in the upper section
        self.assertEqual(Scoreboard.apply_bonus(mrs_test), {"upper_bonus": 35, "yahtzee_bonus": None})

    def test_dont_apply_bonus(self):
        mrs_test = Scoreboard("Mrs Test")
        mrs_test.add_score(('aces', 1))
        mrs_test.add_score(('twos', 2))
        mrs_test.add_score(('threes', 3))
        mrs_test.add_score(('fours', 4))
        mrs_test.add_score(('fives', 5)) #Mrs Test has scored 15 points in the upper section
        self.assertEqual(Scoreboard.apply_bonus(mrs_test), {"upper_bonus": None, "yahtzee_bonus": None})

if __name__ == '__main__':
    unittest.main()