# My command line Yahtzee game - based on the firm family favourite in my house, the dice game of Yahtzee.

from scoreboard import Scoreboard
from calculator import Calculator
import random

class Play_game():
    def __init__(self):
        self.players = {
            'player1': None,
            'player2': None,
            'player3': None,
            'player4': None,
            'player5': None,
            'player6': None
        }
        self._dice_roll = []
        self.scoreboard_instances = {
            'player1': None,
            'player2': None,
            'player3': None,
            'player4': None,
            'player5': None,
            'player6': None,
        }
    
    def create_scoreboard(self):
        for num, player in enumerate(self.players.keys()):
            if player == "computer":
                self.scoreboard_instances[player] = Scoreboard("computer")
            else:
                player = "player" + str(num)
                self.scoreboard_instances[player] = Scoreboard(player)

    def define_players(self):
        number_of_players = input("Enter the number of players:")
        for num in range(int(number_of_players)):
            player_name = input("Enter player name, type 'computer' to play against the computer:")
            playerid = "player" + str(num+1)
            self.players[playerid] = player_name
        self.players = {instance: player_name for instance, player_name in self.players.items() if player_name != None}
        self.create_scoreboard()
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
    
    def choose_score(self, game_player, results_dict): # make available scores obvious
        if game_player != 'computer':
            # find game player in dictionary
            real_person = [value for key, value in self.players.items() if key == game_player]
            print(real_person[0], game_player.__str__()) # printing the scoreboard
            print(real_person, "your dice roll is", self._dice_roll)
            print("Your score options are:")
            for num, key, value in enumerate(results_dict.items()):
                print(num, key, value) #formatted string
            score_choice = input("Enter the number of the score you want to keep:")
            score_choice = int(score_choice)
            score_tuple = list(results_dict.items())[score_choice]
            print("You chose", score_tuple)
            return score_tuple
        else: # computer player always chooses the lowest score != 0 unless the only space in the score dictionary is a score that has a zero then it selectes the first available score
            computer_player = [key for key, value in self.players.items() if value == 'computer']
            computer = [value for key, value in self.scoreboard_instances.items() if key == computer_player[0]]
            computer_scoreboard = computer.getscore_dict()
            zero_removed = {k: v for k, v in results_dict.items() if v != 0}
            score_tuple = min(zero_removed.items(), key=lambda x: x[1])
            while computer_scoreboard[score_tuple[0]] != None:
                zero_removed.pop(score_tuple[0])
                score_tuple = min(zero_removed.items(), key=lambda x: x[1])
                if len(zero_removed) == 0:
                    score_tuple = min(results_dict.items(), key=lambda x: x[1])
                    while computer.scoreboard[score_tuple[0]] != None:
                        results_dict.pop(score_tuple[0])
                        score_tuple = min(results_dict.items(), key=lambda x: x[1])
            return score_tuple

    def play_game(self):
        print("Welcome to Yahtzee!")
        self.define_players()
        print("Let's play!")
        
        for turn in range(1, 13):
            for game_player in self.players:
                if game_player == 'computer':
                    dice_roll = [random.randrange(1, 7) for i in range(0, 5)]
                    self._dice_roll = dice_roll
                else:
                    dice_roll = input("Enter your dice roll, 5,4,3,2,1")
                    self._dice_roll = self.validate_dice_roll_input(dice_roll)
            results_dict = Calculator.calculator(dice_roll)
            # returns a dictionary of score possibilities

            # send score choices to method to offer choices and return a tuple
            score_tuple = self.choose_score(game_player, results_dict)
			
    # it got confusing when trying to create scoreboard instances to players and players started getting renamed - I need to think on this problem
    # maybe just have player 1 and the players define the number of players and then always have a computer player. It is 8pm I really need to stop for the day.
    
	# 	choose the result you want to keep from the calculator scores 
 
	# 	set the computer to choose the result it wants to keep from the calculator scores
 
    # call the apply score
    
	# call the grand total function
    
    # determine winner

if __name__ == "__main__":
	game = Play_game()
	game.play_game()