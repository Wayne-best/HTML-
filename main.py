import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(400,400)
polygon = turtle.Turtle()
side=6
length=90

angle=360.0/side
for i in range(side):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()

