from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake xensia")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "z")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:

        #if segment == snake.head:
            #pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset


#segment_1 = Turtle(shape="square")
#segment_1.color("white")

#segment_2 = Turtle(shape="square")
#segment_2.color("white")
#segment_2.goto(-20,0)

# segment_3= Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40,0)











screen.exitonclick()