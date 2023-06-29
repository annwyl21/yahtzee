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
        
    def validate_dice_roll_input(self, dice_roll):
        dice_roll = [int(dice) for dice in dice_roll.split()]
        return dice_roll
    
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
                    dice_roll = input("Enter your dice roll, 5 4 3 2 1")
                    self._dice_roll = self.validate_dice_roll_input(dice_roll)
				
			
    
	# 	choose the result you want to keep from the calculator scores 
 
	# 	set the computer to choose the result it wants to keep from the calculator scores
 
    # call the apply score
    
	# call the grand total function
    
    # determine winner

if __name__ == "__main__":
	game = Play_game()
	game.play_game()