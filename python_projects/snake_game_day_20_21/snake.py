MOVE_DISTANCE=20
from turtle import Turtle
up=90
down=270
left=180
right=0
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.timmy=[]
        self.create_snake()
        self.head=self.timmy[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)



    def add_segment(self,position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.timmy.append(tim)

    def extend(self):
        self.add_segment(self.timmy[-1].position())



    def move(self):
        for seg_num in range(len(self.timmy) - 1, 0, -1):
            new_x = self.timmy[seg_num - 1].xcor()
            new_y = self.timmy[seg_num - 1].ycor()
            self.timmy[seg_num].goto(new_x, new_y)
        self.timmy[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)




