from turtle import Turtle
import os
import sys
# Add this helper function at the top of the file
def resource_path(filename):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp directory
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.file_path = resource_path("new_file")
        # self.highscore = 0
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                f.write("0")

        with open(self.file_path, mode="r") as newr:
            content = newr.read()
            self.highscore = int(content) if content.strip().isdigit() else 0
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
            with open(self.file_path,mode="w") as new:
                new.write(str(self.highscore))
        self.score = 0
        self.update_score()
