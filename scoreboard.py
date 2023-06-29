
class Scoreboard:
	def __init__(self, name):
		self.player_name = name
		self._score_dict = {"aces": None,
                             "twos": None,
                             "threes": None,
                             "fours": None,
                             "fives": None,
                             "sixes": None,
                             "three_of_a_kind": None,
                             "four_of_a_kind": None,
                             "full_house": None,
                             "sm_straight": None,
                             "lg_straight": None,
			     			 "chance": None,
                             "yahtzee": None,
			     			 "yahtzee_bonus_rolls": []
                             }
		self._bonus_dict = {"upper_bonus": None,
		     				"yahtzee_bonus": None
		     }

	def add_score(self, score_tuple):
		try:
			if self._score_dict[score_tuple[0]] == None:
				self._score_dict[score_tuple[0]] = score_tuple[1]
			else:
				raise ValueError
		except ValueError:
			print("Score already entered for this category.")
		return self._score_dict
	
	def getscore_dict(self):
		return self._score_dict
	
	def apply_bonus(self):
		upper_score = sum([self._score_dict[key] for key in self._score_dict.keys() if key in ["aces", "twos", "threes", "fours", "fives", "sixes"]])
		if upper_score >= 63:
			self._bonus_dict["upper_bonus"] = 35
		else:
			self._bonus_dict["upper_bonus"] = 0
		yahtzee_rolls = len(self._score_dict["yahtzee_bonus_rolls"])
		self._bonus_dict["yahtzee_bonus"] = 100*(yahtzee_rolls)
		return self._bonus_dict
	
	def __repr__(self):
		return f"{self.player_name} Scoreboard {self._score_dict}"
    