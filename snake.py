from turtle import Turtle

STARTING_POSITIONS = starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for block_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[block_num - 1].xcor()
            new_y = self.segments[block_num - 1].ycor()
            self.segments[block_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
