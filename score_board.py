from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "bold"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "bold"))