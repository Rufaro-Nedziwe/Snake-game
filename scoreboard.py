from turtle import Turtle

#import random

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score={self.score}, Highest Score = {self.high_score}", align="right", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

        # def game_over(self):
        #     random_x = random.randint(-280, 280)
        #     random_y = random.randint(-280, 280)
        #     self.goto(random_x, random_y)
        #     self.write("GAME OVER!", align="left", font=("Arial", 24, "normal"))
