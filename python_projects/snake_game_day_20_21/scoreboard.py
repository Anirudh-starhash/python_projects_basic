from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",24,"normal")
INITIAL_POSITION=(-60,260)
HIGH_SCORE_POSITION=(160,260)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=self.get_value()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def get_value(self):
        f=open("me.txt","r")
        a=int(f.read())
        f.close()
        return a

    def update(self):
        self.goto(INITIAL_POSITION)
        self.write(f"Score {self.score}",align=ALIGNMENT, font=FONT)
        self.print()
    def print(self):
        self.goto(HIGH_SCORE_POSITION)
        self.write(f"High Score {self.high_score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.clear()
        self.update()
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNMENT,font=FONT)
        if self.score>self.high_score:
            self.high_score=self.score
            f=open("me.txt",'w')
            f.write(str(self.high_score))
            f.close()






    def increase_score(self):
        self.score+= 1
        self.clear()
        self.goto(INITIAL_POSITION)
        self.update()


