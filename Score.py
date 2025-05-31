from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # self.highscore = 0
        with open("new_file",mode="r") as newr:
            content = newr.read()
            self.highscore = int(content)
            # if content != "":
            #     self.highscore = int(content)
            # else:
            #     self.highscore = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Move to top of the screen
        self.hideturtle()
        self.update_score()





    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}", align="center", font=("Arial", 16, "normal"))

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("new_file",mode="w") as new:
                new.write(str(self.highscore))
        self.score = 0
        self.update_score()
