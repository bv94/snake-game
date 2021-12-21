import turtle
import random


class Food(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(0.5, 0.5)
		self.screen = turtle.Screen()
		self.screen.tracer(0)
		self.color("green")

	def spawn(self, snake):
		if snake.body[0].distance(self) < 15:
			self.goto(random.randint(-280, 280), random.randint(-280, 280))
			self.screen.update()
