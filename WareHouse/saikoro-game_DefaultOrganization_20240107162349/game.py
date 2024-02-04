'''
This file contains the Game class.
'''
from dice import Dice
from player import Player
class Game:
    def __init__(self):
        self.dice = Dice()
        self.players = []
    def add_player(self, name):
        player = Player(name)
        self.players.append(player)
    def start(self):
        for player in self.players:
            print(f"{player.name}'s turn:")
            roll = self.dice.roll()
            print(f"Rolled: {roll}")
            player.add_score(roll)
            print(f"{player.name}'s score: {player.score}")
            print()
        winner = self.get_winner()
        print(f"The winner is {winner.name} with a score of {winner.score}!")
    def get_players(self):
        return self.players
    def get_winner(self):
        return max(self.players, key=lambda player: player.score)
    def reset_scores(self):
        for player in self.players:
            player.score = 0