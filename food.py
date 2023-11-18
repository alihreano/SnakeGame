from turtle import  Turtle
import random
class Food(Turtle): #our new class inherits the turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle") #the default is 20x20
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5) #so the circle is 10x10
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        rand_x=random.randint(-280,280)
        rand_y=random.randint(-280,280)
        self.goto(rand_x,rand_y)
