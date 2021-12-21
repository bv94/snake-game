import turtle
import time


class Snake:
	def __init__(self, ):
		self.body = []
		self.screen = turtle.Screen()
		self.screen.setup(800, 800)
		self.screen.listen()
		self.screen.tracer(0)
		self.screen.bgcolor("black")
		for i in range(4):
			self.body.append(turtle.Turtle("square"))
			self.body[i].color("white")
			self.body[i].penup()
			self.body[i].backward(20 * i)
		self.screen.update()

	def update(self):
		self.screen.update()

	def move(self, ):
		# self.body[0].forward(5)
		for segment in range(len(self.body) - 1, 0, -1):
			self.body[segment].goto(self.body[segment - 1].xcor(), self.body[segment - 1].ycor())
		self.body[0].forward(16)
		time.sleep(0.1)
		self.update()

	def left(self):
		if self.body[0].heading() != 0:
			self.body[0].setheading(180)

	def right(self):
		if self.body[0].heading() != 180:
			self.body[0].setheading(0)

	def up(self):
		if self.body[0].heading() != 270:
			self.body[0].setheading(90)

	def down(self):
		if self.body[0].heading() != 90:
			self.body[0].setheading(270)

	def right_or_left(self):
		self.screen.onkey(self.right, "Right")
		self.screen.onkey(self.left, "Left")
		self.screen.onkey(self.up, "Up")
		self.screen.onkey(self.down, "Down")

	def game_on(self):
		self.right_or_left()
		self.move()

	def extend(self):
		self.body.append(turtle.Turtle("square"))
		self.body[-1].color("white")
		self.body[-1].penup()
		self.body[-1].goto(self.body[-2].xcor(), self.body[-2].ycor())

	def collision_handler(self):
		for segment in self.body:
			if segment == self.body[0]:
				pass
			elif segment.distance(self.body[0]) < 14:
				return True

# snake = Snake()
# while True:
# 	snake.game_on()dd
#
# snake.screen.exitonclick()
