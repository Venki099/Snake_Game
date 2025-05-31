from turtle import Turtle
position = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class SnakeGame:

    def __init__(self):
        print("hi")
        self.newTurtle = []
        self.create_snake()
        self.head = self.newTurtle[0]

    def create_snake(self):
        for i in range(0, 3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position[i])
            self.newTurtle.append(new_turtle)

    def move(self):
        # for seg in newturtles:
        #     seg.forward(20)
        for seg_num in range(len(self.newTurtle) - 1, 0, -1):
            new_x = self.newTurtle[seg_num - 1].xcor()
            new_y = self.newTurtle[seg_num - 1].ycor()
            self.newTurtle[seg_num].goto(new_x, new_y)
        # new_turtle.forward(20)
        self.newTurtle[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.newTurtle[0].heading() != DOWN:
            self.newTurtle[0].setheading(UP)

    def down(self):
        if self.newTurtle[0].heading() != UP:
            self.newTurtle[0].setheading(DOWN)

    def right(self):
        if self.newTurtle[0].heading() != LEFT:
            self.newTurtle[0].setheading(RIGHT)

    def left(self):
        if self.newTurtle[0].heading() != RIGHT:
            self.newTurtle[0].setheading(LEFT)

    def increaselength(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        self.newTurtle.append(new_turtle)

    def reset(self):
        for snake in self.newTurtle:
            snake.goto(1000,1000)
        self.newTurtle.clear()
        self.create_snake()
        self.head = self.newTurtle[0]
