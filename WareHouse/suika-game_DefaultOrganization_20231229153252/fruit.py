'''
This file contains the Fruit class which represents a fruit in the game.
'''
import tkinter as tk
class Fruit:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 50
        self.color = "red"
        self.oval = self.draw()
    def draw(self):
        return self.canvas.create_oval(self.x - self.size/2, self.y - self.size/2,
                                       self.x + self.size/2, self.y + self.size/2,
                                       fill=self.color)
    def contains(self, x, y):
        return (self.x - self.size/2 <= x <= self.x + self.size/2 and
                self.y - self.size/2 <= y <= self.y + self.size/2)
    def evolve(self):
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
        current_color_index = colors.index(self.color)
        next_color_index = (current_color_index + 1) % len(colors)
        self.color = colors[next_color_index]
        self.canvas.itemconfig(self.oval, fill=self.color)