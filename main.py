import snake
import food
import scoreboard

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()
game_is_on = True
while game_is_on:

	snake.game_on()
	if snake.body[0].distance(food) < 15:
		snake.extend()
		food.spawn(snake)
		scoreboard.score_handler(snake, food)
	if snake.body[0].xcor() > 280 or snake.body[0].xcor() < -280 or snake.body[0].ycor() > 280 or snake.body[
		0].ycor() < -280 or snake.collision_handler():

		game_is_on = False
		scoreboard.game_over()

snake.screen.exitonclick()
