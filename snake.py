from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_SEGMENTS = 3
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")

    def create_segment(self, x, y):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.speed(1)
        turtle.penup()
        turtle.setx(x=x)
        turtle.sety(y=y)
        self.segments.append(turtle)

    def create_snake(self):
        for i in range(STARTING_SEGMENTS):
            self.create_segment(i * -20, 0)

    def move(self):
        for segment in reversed(self.segments):
            i = self.segments.index(segment)
            if i != 0:
                x = self.segments[i - 1].xcor()
                y = self.segments[i - 1].ycor()
                segment.setpos(x, y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        x = (self.segments[-1].xcor())
        y = (self.segments[-1].ycor())
        self.create_segment(x, y)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)