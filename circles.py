import turtle
turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0)
for i in range(5):
    for colors in["blue","red","green","orange","magenta","yellow","white","cyan"]:
        turtle.color(colors)
        turtle.circle(200)
        turtle.left(10)
turtle.hideturtle()
