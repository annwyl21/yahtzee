from scoreboard import Scoreboard    # The code to test
import unittest   # The test framework

class Test_TestScoreboard(unittest.TestCase):
    def test_get_scoreboard(self):
        # how do I feed in the multiple scores into add score to get this result?
        self.assertEqual(Scoreboard.get_scoreboard(), {'aces': 0, 'twos': 0, 'threes': 3, 'fours': 4, 'fives': 15, 'sixes': 0, 'three_of_a_kind': 15, 'four_of_a_kind': 0, 'full_house': 0, 'sm_straight': 0, 'lg_straight': 0, 'yahtzee': 0, 'chance': 22})
        #if I call the scoreboard, the test returns a hard-coded scoreboard

	def test_add_score(self):
        self.assertEqual(Scoreboard.add_score(('threes', 3)), {'aces': 0, 'twos': 0, 'threes': 3, 'fours': 0, 'fives': 0, 'sixes': 0, 'three_of_a_kind': 0, 'four_of_a_kind': 0, 'full_house': 0, 'sm_straight': 0, 'lg_straight': 0, 'yahtzee': 0})
        #if I add a score to the scoreboard, the test returns a scoreboard with that score added
	
	def test_dont_add_score(self):
        self.assertEqual(Scoreboard.add_score(('threes', 9)), {'aces': 0, 'twos': 0, 'threes': 3, 'fours': 0, 'fives': 0, 'sixes': 0, 'three_of_a_kind': 0, 'four_of_a_kind': 0, 'full_house': 0, 'sm_straight': 0, 'lg_straight': 0, 'yahtzee': 0})
        #if I try to add a score to the scoreboard that already exists, the test returns a scoreboard with the original score still there

if __name__ == '__main__':
    unittest.main()