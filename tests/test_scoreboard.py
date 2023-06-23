from scoreboard import Scoreboard    # The code to test
import unittest   # The test framework

@pytest.fixture
def create_instance():
   mrs_test = Scoreboard("Mrs_Test")

@pytest.fixture(create_instance)
class Test_TestScoreboard(unittest.TestCase):
    def test_get_scoreboard(self):
        # how do I feed in the multiple scores into add score to get this result?
        #mrs_test = Scoreboard("Mrs_Test")
        self.assertEqual(Scoreboard.getscore_dict(mrs_test), {'aces': None, 'twos': None, 'threes': None, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None})
        #if I call the scoreboard, the test returns an empty scoreboard

    # def test_add_score(self):
    #     self.assertEqual(Scoreboard.add_score('test', ('threes', 3)), {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None})
    #     #if I add a score to the scoreboard, the test returns a scoreboard with that score added

    # def test_dont_add_score(self):
    #     self.assertEqual(Scoreboard.add_score('test', ('threes', 9)), {'aces': None, 'twos': None, 'threes': 3, 'fours': None, 'fives': None, 'sixes': None, 'three_of_a_kind': None, 'four_of_a_kind': None, 'full_house': None, 'sm_straight': None, 'lg_straight': None, 'chance': None, 'yahtzee': None})
    #     #if I try to add a score to the scoreboard that already exists, the test returns a scoreboard with the original score still there

if __name__ == '__main__':
    
    unittest.main()