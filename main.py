from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
from wall import Wall
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
wall = Wall()
score_board = Scoreboard()
screen.tracer(2)

screen.onkey(key="w", fun=snake.move_forward)
screen.onkey(key="d", fun=snake.turn_right)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="s", fun=snake.move_backward)

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.eaten()
        score_board.increase_score()
        snake.add_block_to_snake()
        food = Food()

    if (((snake.head.xcor() > 280 or
            snake.head.xcor() < -280) or
            snake.head.ycor() > 280) or
            snake.head.ycor() < -280):
        print("You lose")
        is_on = False
        score_board.highest_score()
        score_board.clear()
        score_board.game_over()

    screen.listen()
screen.exitonclick()
