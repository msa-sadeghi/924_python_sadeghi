import turtle
import random
from time import sleep



main_screen = turtle.Screen()
main_screen.setup(600, 600)
main_screen.bgcolor("black")
main_screen.title("SnakeGame")
main_screen.tracer(False)

def create_turtle(shape, color):
    my_turtle = turtle.Turtle()
    my_turtle.shape(shape)
    my_turtle.color(color)
    my_turtle.penup()
    return my_turtle

def change_position(object):
    x = random.randint(-270, 270)
    y = random.randint(-270, 240)
    object.goto(x,y)

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)

def go_up():
    snake_head.direction = "up"

def go_down():
    snake_head.direction = "down"

def go_left():
    snake_head.direction = "left"

def go_right():
    snake_head.direction = "right"

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")

change_position(snake_food)


score = 0
scoreboard = create_turtle("square", "white")
scoreboard.goto(0, 260)
scoreboard.ht()

main_screen.listen()
main_screen.onkeypress(go_up, "Up")
main_screen.onkeypress(go_down, "Down")
main_screen.onkeypress(go_left, "Left")
main_screen.onkeypress(go_right, "Right")


while True:
    scoreboard.clear()
    scoreboard.write(f"Score:{score}", font=("arial",22), align="center")
    main_screen.update()
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        score += 1
        
    move()
    sleep(0.2)