from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Python Snake Game')
my_screen.tracer(0)
is_movement = True

snake = Snake()
food = Food()
score_board = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, 'Up')
my_screen.onkey(snake.down, 'Down')
my_screen.onkey(snake.left, 'Left')
my_screen.onkey(snake.right, 'Right')

while is_movement:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food(circle)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.add_score()

    # Detect collision with wall boarders
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision btw head and tail
    for snake_body in snake.segments:
        if snake_body == snake.head:
            pass
        elif snake.head.distance(snake_body) < 10:
            score_board.reset()
            snake.reset()

my_screen.exitonclick()
