# My command line Yahtzee game - based on the firm family favourite in my house, the dice game of Yahtzee.

from scoreboard import Scoreboard
from calculator import Calculator
import random

class Play_game():
    def __init__(self):
        self.players = []
        _dice_roll = []
    
    def define_players(self):
        print("Enter the names of the players. Enter 'Computer' to play against the computer.")
        player_name = ""
        while player_name != "done":
            player_name = input("Enter player name or type 'done' to start game:")
            if player_name == "done":
                break
            else:
                self.players.append(player_name)
            if len(self.players) == 6:
                print("Maximum number of players is 6.")
                break
        for player in self.players:
            player = Scoreboard(player)
        print(f"Players are: {self.players}")
        
    # maybe have another validation class that does this work    
    def validate_dice_roll_input(self, dice_roll):
        try:
            dice_roll = [int(dice) for dice in dice_roll.split(',')]
            if len(dice_roll) == 1:
                unpack_dice_roll = [int(num) for num in str(dice_roll[0])]
                if len(unpack_dice_roll) == 5:
                    dice_roll = unpack_dice_roll
            return dice_roll
        except:
            dice_roll = [int(dice) for dice in dice_roll.split()]
            if len(dice_roll) == 5:
                return dice_roll
            else:
                print("ERROR: data entry error")
    
    def choose_score(player, results_dict):
        if player.lower() != 'computer':
            print(player.__str__()) # printing the scoreboard
            # need to print the results dictionary
            # and get the player to select a result that can be converted into a score tuple and sent in to the scoreboard
        #then handle computer player

    def play_game(self):
        print("Welcome to Yahtzee!")
        self.define_players()
        print("Let's play!")
        
        for turn in range(1, 13):
            for player in self.players:
                if player.lower() == 'computer':
                    dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
                    self._dice_roll = dice_roll
                else:
                    dice_roll = input("Enter your dice roll, 5,4,3,2,1")
                    self._dice_roll = self.validate_dice_roll_input(dice_roll)
            results_dict = Calculator.calculator(dice_roll)
            # returns a dictionary of score possibilities
            # send score choices to method to offer choices and return a tuple
            score_tuple = self.choose_score(player, results_dict)
			
    
	# 	choose the result you want to keep from the calculator scores 
 
	# 	set the computer to choose the result it wants to keep from the calculator scores
 
    # call the apply score
    
	# call the grand total function
    
    # determine winner

if __name__ == "__main__":
	game = Play_game()
	game.play_game()