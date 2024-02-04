'''
This file contains the Player class.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def add_score(self, points):
        self.score += points