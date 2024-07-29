from turtle import Turtle

FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-85,350)
        self.write(f"Score: {self.score}", move=False, align='left', font=FONT)
        
        self.hideturtle()
        
        
    
    def update(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=FONT)
    
    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over!", move=False, align='center', font=FONT)