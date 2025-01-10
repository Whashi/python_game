from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
turtle = Turtle()
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

on = True
screen.update()

def game_over():
    turtle.hideturtle()
    turtle.color("white")
    turtle.write("Game Over", align="center", font=("Arial", 36, "bold"))
    return False

while on:
    screen.update()
    time.sleep(0.12)

    snake.move()
    for segment in range(1, len(snake.segments)):
        seg_cor = (round(snake.segments[segment].xcor()), round(snake.segments[segment].ycor()))
        head_cor = (round(snake.head.xcor()), round(snake.head.ycor()))
        if seg_cor == head_cor:
            on = game_over()

    if snake.head.distance(food) < 15:
        score_board.add_point()
        snake.add_segment()
        food.refresh()

    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        on = game_over()

screen.exitonclick()
