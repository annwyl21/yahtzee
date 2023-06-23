class Scoreboard:
    def __init__(self, player_name):
        self.player_name = ""
        self._score_dict = {"aces": 0,
                             "twos": 0,
                             "threes": 0,
                             "fours": 0,
                             "fives": 0,
                             "sixes": 0,
                             "three_of_a_kind": 0,
                             "four_of_a_kind": 0,
                             "full_house": 0,
                             "sm_straight": 0,
                             "lg_straight": 0,
                             "yahtzee": 0
                             }
	
	def add_score(self, score_tuple):
		try:
			if score_dict[score_tuple[0]] == 0:
				self._score_dict[score_tuple[0]] = score_tuple[1]
			else:
				raise ValueError
		except ValueError:
			print("Score already entered for this category.")
		return self._score_dict
	
	def get_scoreboard(self):
		return self._score_dict
	
	def __str__(self):
		return f"{self.player_name} Scoreboard {self._score_dict}"
	
	def __repr__(self):
		return f"{self.player_name} Scoreboard {self._score_dict}"

if __name__ == '__main__':
    #create an instance of a player's scoreboard
	player1 = Scoreboard("Player1")

	#add scores in tuples to the scoreboard for each turn of play
	player1.add_score(('threes', 3))
	player1.add_score(('fours', 4))
	player1.add_score(('fives', 15))
	player1.add_score(('three_of_a_kind', 15))
	player1.add_score(('chance', 22))

	print(str(player1))
	print(repr(player1))
    