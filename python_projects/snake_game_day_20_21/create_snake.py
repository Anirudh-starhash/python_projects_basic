from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
is_game_on=True
screen.listen()
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_on=False
        scoreboard.game_over()

    #detect collision with tail

    for segment in snake.timmy[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            scoreboard.game_over()











screen.exitonclick()
