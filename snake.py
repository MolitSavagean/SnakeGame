from turtle import Turtle

XY_COR = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for x in XY_COR:
            self.add_segment(x)

    def add_segment(self, x):
        t = Turtle('square')
        t.color("white")
        t.penup()
        t.goto(x)
        self.all_turtle.append(t)

    def extend(self):
        self.add_segment(self.all_turtle[-1].position())

    def reset(self):
        for seg in self.all_turtle:
            seg.goto(1000, 1000)
        self.all_turtle.clear()
        self.create_snake()
        self.head = self.all_turtle[0]

    def move(self):
        for num in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[num - 1].xcor()
            new_y = self.all_turtle[num - 1].ycor()
            self.all_turtle[num].goto(new_x, new_y)
        self.head.fd(MOVE_DIST)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
