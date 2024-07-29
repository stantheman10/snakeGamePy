from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    
    def __init__(self):
        """Initialize the snake class"""
        self.segments = []
        self.create_snake()
        
    
    def create_snake(self):
        """Creates snake with 3 squares"""
        for position in STARTING_POSITION:
            
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    
    def snake_move(self):
        """Moves the snake forward"""
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        """Makes the snake move north direction"""
        self.segments[0].setheading(90)
        self.snake_move()
    def down(self):
        """Makes the snake move south direction"""
        self.segments[0].setheading(270)
        self.snake_move()
        
    def left(self):
        """Makes the snake move west direction"""
        self.segments[0].setheading(180)
        self.snake_move()
    
    def right(self):
        """Makes the snake move east direction"""
        self.segments[0].setheading(0)
        self.snake_move()
        
    
        