from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        with open("highest_score.txt", "r") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score is : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.write(f"GAME OVER! YOUR SCORE IS: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.goto(0, 0)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def highest_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.update_score()

