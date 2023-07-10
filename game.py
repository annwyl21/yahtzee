# My command line Yahtzee game - based on the firm family favourite in my house, the dice game of Yahtzee.

from scoreboard import Scoreboard
from calculator import Calculator
import random
import sys

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
            print('Results of dice roll for computer')
            for num, key in enumerate(results_dict.keys(), 1):
                print(f"{num:2d} Result:{key:<10s} {results_dict[key]}")
            # 1st available option on scoreboard - computer is not playing to win
            for key, score in scoreboard.items():
                if score == None:
                    score_tuple = key, results_dict[key]
                    print(f'Computer chose {score_tuple}')
                    return score_tuple
        else:
            scoreboard = self.player.getscore_dict()
            print('Results of dice roll for player')
            for num, key in enumerate(results_dict.keys(), 1):
                print(f"{num:2d} Result:{key:<10s} {results_dict[key]}")
            # player selects their dice result to add to their scoreboard
            selected_result = input('Choose the result you wish to add to your scoreboard, type a number:\n')
            for num, key in enumerate(results_dict.keys(), 1):
                if num == int(selected_result):
                    score_tuple = key, results_dict[key]
                    print(f'Player chose {score_tuple}')
                    results_tuple = score_tuple, results_dict["yahtzee_bonus"]
                    return results_tuple

    def scoring(self):
        # display scoreboard
        player_scoreboard = self.player.getscore_dict()
        computer_scoreboard = self.computer.getscore_dict()

        print('Scores so far:\nComputer vs Player...')
        for key in player_scoreboard:
            print(f"{key:<20s}  {computer_scoreboard[key]}  {key:<20s}  {player_scoreboard[key]}")

        # display bonuses
        player_bonus = self.player.apply_bonus()
        print(f'Player bonus scores:\n {player_bonus}')
        computer_bonus = self.computer.apply_bonus()
        print(f'Computer bonus scores:\n {computer_bonus}')

        # declare winner and display grand total
        computer_end_score = self.computer.grand_total()
        player_end_score = self.player.grand_total()
        if computer_end_score == player_end_score:
            print(f'DRAW {computer_end_score}:{player_end_score}')
        elif computer_end_score > player_end_score:
            print(f'Computer won {computer_end_score}:{player_end_score}')
        else:
            print(f'Congratulations YOU WON! {computer_end_score}:{player_end_score}')
        return player_end_score


    def play_game(self):
        print("Welcome to Yahtzee!")
        print("Let's play!")
        
        for turn in range(1, 14):
            for game_player in self.players:
                if game_player == 'computer':
                    self._dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
                else:
                    dice_roll_input = input("Enter your dice roll, 5,4,3,2,1:\n")
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

        print('Goodbye\n')
        sys.exit()

if __name__ == "__main__":
	game = Play_game()
	game.play_game()