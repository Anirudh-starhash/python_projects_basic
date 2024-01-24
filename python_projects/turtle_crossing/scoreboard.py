FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("green")
        self.penup()
        self.hideturtle()
        self.print()

    def increase_level(self):
        self.level+=1
        self.clear()
        self.print()

    def print(self):
        self.goto(-280, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.clear()
        self.goto(0,0)
        self.color("black")
        self.write(f"Game Over",align="center",font=FONT)

