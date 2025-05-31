import time
from turtle import Screen
from Snake import SnakeGame
from Food import Food
from Score import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
pos = 0

screen.tracer(0)
snake = SnakeGame()
food = Food()
score = ScoreBoard()
    # pos -= 20
# print(newturtles)

screen.listen()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)
game_is_on = True
while game_is_on:
    score.penup()
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        # print("nom nom")
        food.foodpos()
        score.increase_score()
        snake.increaselength()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # score.gameover()
        score.reset()
        snake.reset()
    for segment in snake.newTurtle[1:]:
        # if segment == snake.head:
        #     pass

        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.gameover()
            score.reset()
            snake.reset()
    # newturtles[0].right(90)
screen.exitonclick()