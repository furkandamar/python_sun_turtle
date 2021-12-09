import turtle
turtle.title('Youtube : Derinlemesine Yazılım')
turtle.setup(width=300, height=500)

bob = turtle.Turtle(shape='turtle')
bob.color('orange')

# Drawing a filled star thingy
bob.speed(2000)
bob.fillcolor('yellow')
bob.pencolor('red')

for i in range(100):

    bob.begin_fill()
    bob.forward(100 - i)
    bob.left(150)
    bob.forward(100 - i)
    bob.end_fill()

turtle.exitonclick()
