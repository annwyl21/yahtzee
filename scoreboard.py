
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
		self._bonus_dict = {"upper_bonus": 0,
		     				"yahtzee_bonus": 0
		     }

	def add_score(self, results_tuple):
		score_tuple = results_tuple[0]
		try:
			if self._score_dict[score_tuple[0]] == None:
				self._score_dict[score_tuple[0]] = score_tuple[1]
			else:
				raise ValueError
		except ValueError:
			print("Score already entered for this category.")
		if results_tuple[1] == True:
			self._score_dict["yahtzee_bonus_rolls"].append('X')
		return self._score_dict
	
	def getscore_dict(self):
		return self._score_dict
	
	def apply_bonus(self):
		upper_score = sum([self._score_dict[key] for key in self._score_dict.keys() if key in ["aces", "twos", "threes", "fours", "fives", "sixes"]])
		if upper_score >= 63:
			self._bonus_dict["upper_bonus"] = 35
		else:
			self._bonus_dict["upper_bonus"] = 0
		if len(self._score_dict["yahtzee_bonus_rolls"]):
			num_yahtzee_rolls = len(self._score_dict["yahtzee_bonus_rolls"])
			if num_yahtzee_rolls > 3:
				yahtzee_rolls = 3
			else:
				yahtzee_rolls = num_yahtzee_rolls
		else:
			yahtzee_rolls = 0
		self._bonus_dict["yahtzee_bonus"] = 100*(yahtzee_rolls)
		return self._bonus_dict

	def grand_total(self):
		try:
			grand_total = sum([self._score_dict[key] for key in self._score_dict.keys() if key in ["aces", "twos", "threes", "fours", "fives", "sixes", "three_of_a_kind", "four_of_a_kind", "full_house", "sm_straight", "lg_straight", "chance", "yahtzee"]]) + self._bonus_dict["upper_bonus"] + self._bonus_dict["yahtzee_bonus"]
			return grand_total
		except TypeError:
			print("Not all scores have been entered yet, some still have 'None' values.")
	
	def __repr__(self):
		return f"Scoreboard {self._score_dict}"
	
	def __str__(self) -> str:
		return f"Your current scoreboard {self._score_dict}"
    