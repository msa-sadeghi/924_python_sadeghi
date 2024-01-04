from turtle import Turtle,Screen,done

screen = Screen()
screen.bgcolor('orange')
screen.register_shape('strawberry.gif')
# screen.bgpic("img.png")
my_turtle = Turtle()
my_turtle.shape('turtle') # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
my_turtle.shape('strawberry.gif')
my_turtle.shapesize(3)
my_turtle.color("green")
my_turtle.pencolor("red")
my_turtle.pensize(4)

sides = int(screen.textinput("sides","How many sides?"))

for i in range(sides):
    my_turtle.forward(100)
    my_turtle.left(360/sides)

done()