from turtle import Turtle


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.goto(0, 270)
		self.score = 0
		self.color("green")
		self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

	def score_handler(self, snake, food):
		self.score += 1
		self.clear()
		self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

	def game_over(self):
		self.setheading(270)
		self.goto(0,0)
		self.write("game over", align="center", font=("Arial", 24, "normal"))
