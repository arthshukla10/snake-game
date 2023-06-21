from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scorecard import Scoreboard
import time
screen=Screen()
screen.setup(width=550,height=550)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food=Food()
scorecard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        
        scorecard.increase_score()


     #wall
    if snake.segment[0].xcor() >260 or snake.segment[0].xcor()<-260 or snake.segment[0].ycor()>260 or snake.segment[0].ycor()<-260:
        game_on=False
        scorecard.game_over()

    for segment in snake.segment:
        if segment == snake.segment[0]:
            pass
        elif snake.segment[0].distance(segment)<10:
            game_on=False
            scorecard.game_over()









screen.exitonclick()