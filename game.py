# My command line Yahtzee game - based on the firm family favourite in my house, the dice game of Yahtzee.

from scoreboard import Scoreboard
from calculator import Calculator
import random
import sys
import re

class Play_game():
    def __init__(self):
        self.players = {'computer', 'player'}
        self._dice_roll = []
        self._yahtzee = False
        self.computer = Scoreboard('computer')
        self.player = Scoreboard('player')
        
    # maybe have another validation class that does this work    
    def validate_dice_roll_input(self, dice_roll):
        try:
            dice_roll_int = [int(dice) for dice in dice_roll.split(',')]
            if len(dice_roll_int) == 1:
                return None
            else:
                return dice_roll_int
        except:
                print("ERROR: data entry error")
    
    def choose_score(self, game_player, results_dict):
        if game_player == 'computer':
            scoreboard = self.computer.getscore_dict()
            print('\n' + 50*'=' + '\nCOMPUTER RESULTS:\n')
            for num, key in enumerate(results_dict.keys(), 1):
                print(f"{num:2d} Result:{key:<23s} {results_dict[key]}")
            # 1st available option on scoreboard - computer is not playing to win
            for key, score in scoreboard.items():
                if score == None:
                    score_tuple = key, results_dict[key]
                    print(f'\nComputer chose {score_tuple}')
                    results_tuple = score_tuple, results_dict["yahtzee_bonus"]
                    return results_tuple
        else:
            scoreboard = self.player.getscore_dict()
            print("\nCurrent Scoreboard Status\n")
            # for key, score in scoreboard.items():
            #     print(f"{key:<10s} {score}")
            print('\n' + 50*'+' + '\nPLAYER RESULTS:\n')
            results = [key for key in results_dict if key != "yahtzee_bonus"]
            for num, key in enumerate(results, 1):
                if scoreboard[key] == None:
                    print(f"{num:2d} {key:<23s}Roll Result: {results_dict[key]:3d}, Your Scoreboard {scoreboard[key]}")
                else:
                    print(f"XX {key:<23s}Rolled: {results_dict[key]:8d}, Scoreboard holding {scoreboard[key]}")
            # player selects their dice result to add to their scoreboard
            selected_result = input('\nScore to add:\n')
            for num, key in enumerate(results_dict.keys(), 1):
                if num == int(selected_result):
                    score_tuple = key, results_dict[key]
                    print(f'\nPlayer chose {score_tuple}')
                    results_tuple = score_tuple, results_dict["yahtzee_bonus"]
                    return results_tuple

    def scoring(self):
        # display scoreboard
        player_scoreboard = self.player.getscore_dict()
        computer_scoreboard = self.computer.getscore_dict()

        print('\nScores so far:\nComputer vs Player...\n')
        for key in player_scoreboard:
            print(f"{key:<20s}  {computer_scoreboard[key]}  {key:<20s}  {player_scoreboard[key]}")

        # display bonuses
        player_bonus = self.player.apply_bonus()
        print(f'\nPlayer bonus scores:\n {player_bonus}')
        computer_bonus = self.computer.apply_bonus()
        print(f'\nComputer bonus scores:\n {computer_bonus}')

        # declare winner and display grand total
        computer_end_score = self.computer.grand_total()
        player_end_score = self.player.grand_total()
        if computer_end_score == player_end_score:
            print(f'\nDRAW {computer_end_score}:{player_end_score}')
        elif computer_end_score > player_end_score:
            print(f'\nComputer won {computer_end_score}:{player_end_score}')
        else:
            print(f'\nCongratulations YOU WON! {computer_end_score}:{player_end_score}')
        return player_end_score


    def play_game(self):
        print("\nWelcome to Yahtzee!")
        print("\nLet's play!")
        
        for turn in range(1, 14):
            for game_player in self.players:
                if game_player == 'computer':
                    self._dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
                else:
                    dice_roll_input = ""
                    # check dice roll is valid using regex 
                    while not re.match(r'^([1-6],){4}[1-6]$', dice_roll_input):
                        dice_roll_input = input("\nEnter your dice roll, 5,4,3,2,1:\n")
                    self._dice_roll = self.validate_dice_roll_input(dice_roll_input)
            
                results_dict = Calculator(self._dice_roll).calculator()
                # returns a dictionary of score possibilities

                # Make score choices
                score_tuple = self.choose_score(game_player, results_dict)
                if game_player == 'computer':
                    self.computer.add_score(score_tuple)
                else:
                    self.player.add_score(score_tuple)

        # Turn-taking over - grand total scores
        self.scoring()

        print('\nGoodbye\n')
        sys.exit()

if __name__ == "__main__":
	game = Play_game()
	game.play_game()

# add comments to explain the code