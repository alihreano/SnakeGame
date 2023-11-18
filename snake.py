import time
from turtle import Turtle
MOVE_DISTANCE=20
STARTING_POSITIONS=[(0,0),(0,-20),(0,-40)]
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for pos in STARTING_POSITIONS:  # creating the snake
            self.add_seg(pos)
    def add_seg(self,pos):
        segment = Turtle(shape="square")  # the default is 20x20 and its positioning is (0,0)
        segment.color("white")
        segment.penup()  # so when the snake moves we don't see the line
        segment.goto(pos)
        self.segments.append(segment)
    def extend(self):
        self.add_seg(self.segments[-1].position())
    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)
