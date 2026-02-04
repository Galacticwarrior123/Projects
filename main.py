import turtle

turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 6
angle = 360 / num_sides
side_length=70

for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)

turtle.done()