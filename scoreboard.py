from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 275)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.highscore}",  align=ALIGN, font=FONT)

    def points(self):
        self.score += 1
        self.update_board()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt" , mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_board()




