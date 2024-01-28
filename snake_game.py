import turtle
import random
from time import sleep
import os


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
    if snake_head.direction != "down":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")

change_position(snake_food)


score = 0
if os.path.exists("score.txt"):
    f = open("score.txt", "r")
    highscore = int(f.read())
else:
    highscore = 0
scoreboard = create_turtle("square", "white")
scoreboard.goto(0, 260)
scoreboard.ht()

main_screen.listen()
main_screen.onkeypress(go_up, "Up")
main_screen.onkeypress(go_down, "Down")
main_screen.onkeypress(go_left, "Left")
main_screen.onkeypress(go_right, "Right")

def on_close():
    f = open("score.txt", "w")
    f.write(str(highscore))
    f.close()
    global running
    running = False

root = main_screen._root
root.protocol("WM_DELETE_WINDOW", on_close)


tails = []
running = True
while running:
    scoreboard.clear()
    scoreboard.write(f"Score:{score}, HighScore:{highscore}", font=("arial",22), align="center")
    main_screen.update()
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        score += 1
        if score > highscore:
            highscore = score
        new_tail = create_turtle("square", "darkgreen")
        tails.append(new_tail)

    for i in range(len(tails) - 1, 0, -1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x,y)

    if len(tails):
        tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290:
        snake_head.setx(-1 * snake_head.xcor())

    if snake_head.ycor() > 240:
        snake_head.sety(-290)
    if snake_head.ycor() < -290:
        snake_head.sety(240)
        
    move()

    for t in tails:
        if t.distance(snake_head) < 20:
            snake_head.goto(0,0)
            score = 0
            snake_head.direction = ""
            for t in tails:
                t.ht()
            tails = []
    sleep(0.2)
