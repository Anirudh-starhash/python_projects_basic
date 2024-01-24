from turtle import Turtle,Screen
from paddle import Paddle
from Ball import ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard=Scoreboard()
for i in range(-400,401,20):
    tim=Turtle()
    tim.penup()
    tim.color("white")
    tim.goto(0, i)
    tim.write("|",False,align="center",font=('Arial',24,'normal'))
    tim.hideturtle()


l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
Ball=ball()

is_game_on=True
Ball.move()

while is_game_on:
    time.sleep(Ball.move_speed)
    screen.update()
    Ball.move()

    if Ball.ycor()>280 or Ball.ycor()< -280:
        Ball.bounce_y()

    if r_paddle.distance(Ball)<50 and Ball.xcor()>320 or (l_paddle.distance(Ball)<50 and Ball.xcor()<-320):
        Ball.bounce_x()

    #now if ball misses the paddle score should be updated and game should resume till we want it to go

    if Ball.xcor()>380  or Ball.xcor()<-380:
        if Ball.xcor()>380:
            scoreboard.increase_lscore()
        else:
            scoreboard.increase_rscore()
        Ball.reset_position()

    if scoreboard.lscore==5 or scoreboard.rscore==5:
       is_game_on=False
       scoreboard.gameover()


screen.exitonclick()



