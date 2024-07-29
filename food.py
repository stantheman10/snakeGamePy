from turtle import Turtle
import random
class Food(Turtle):
    """Class to represent food that will be placed on the screen and eaten by the snake"""
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed(10)
        self.rand_x = random.randint(-680,680)
        self.rand_y = random.randint(-680,680)
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x, random_y)