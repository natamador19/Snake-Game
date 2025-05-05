
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on=True

snake = Snake()
food=Food()
score=Scoreboard()

screen.listen()

screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1 )


    snake.move()
    #The snake eats the ball
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.growSnake()
       score.addScore()
    #The snakes collide with a wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset_snake()


    #The snake collide with the tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            score.reset()
            snake.reset_snake()


screen.exitonclick()