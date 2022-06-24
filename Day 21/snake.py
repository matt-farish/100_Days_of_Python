# Day 20 of Udemy's 100 Days of Python programming course
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a starting snake, consisting of three segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        """Adds a segment to the snake using a provided position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Axtends the snake by adding a segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Sets movement of the snake to forward. Head maintains location whilst proceeding segments follow the head."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes the heading of the snake to 90°"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the heading of the snake to 270°"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the heading of the snake to 180°"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the heading of the snake to 0°"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    