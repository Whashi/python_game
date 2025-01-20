from turtle import Turtle

FONT = ("Arial", 12, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, 280)
        self.get_high_score()
        self.update_score()

    def get_high_score(self):
        with open("data.txt") as f:
            self.high_score = f.read()
            return self.high_score

    def update_score(self):
        self.get_high_score()
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)

    def add_point(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as f:
                f.write(str(self.score))
        self.score = 0
        self.update_score()