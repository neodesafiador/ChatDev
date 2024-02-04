'''
This file contains the Game class which manages the game logic.
'''
import tkinter as tk
from fruit import Fruit
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Fruit Evolution Game")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.fruits = []
        self.canvas.bind("<Button-1>", self.on_click)
        self.points = 0
        self.points_label = tk.Label(self.root, text="Points: 0")
        self.points_label.pack()
    def on_click(self, event):
        x, y = event.x, event.y
        for fruit in self.fruits:
            if fruit.contains(x, y):
                fruit.evolve()
                self.points += 1
                self.points_label.config(text="Points: " + str(self.points))
                break
        else:
            self.create_fruit(x, y)
    def create_fruit(self, x, y):
        fruit = Fruit(self.canvas, x, y)
        self.fruits.append(fruit)
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