import time
from turtle import Turtle,Screen
from snake import Snake #import the snake class from the snake file
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") #the background color of the screen
screen.title("SNAKE GAME ON!")
screen.tracer(0) #so the snake body is whole and not in segments! turning the animation off
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen() #to start listeing for key strokes (up/down/left/right arrow keys)
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # collision with food (extinding tail every time it collides):
    if snake.head.distance(food)< 15:
        scoreboard.score_up()
        snake.extend()
        food.refresh()
    #collision with wall:
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()
    #collision with tail:
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game_is_on=False
            scoreboard.game_over()
screen.exitonclick()