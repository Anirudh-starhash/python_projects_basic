from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial',50,'normal')
FONT2=('Arial',24,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore=0
        self.lscore=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.refresh()



    def refresh(self):
        self.goto(-100, 200)
        self.write(f"{self.lscore}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.rscore}", align=ALIGNMENT, font=FONT)

    def increase_lscore(self):
        self.lscore+=1
        self.clear()
        self.refresh()

    def increase_rscore(self):
        self.rscore+=1
        self.clear()
        self.refresh()


    def gameover(self):
        self.penup()
        self.goto(0, 0)
        if(self.lscore==5):
            winner="Player at left side"
        else:
            winner="Player at right side"
        self.write(f"Game Over winner is {winner}", align=ALIGNMENT, font=FONT2)



