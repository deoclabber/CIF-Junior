import turtle

turtle.speed(0)
turtle.delay(0)
turtle.shape("arrow")
turtle.goto(0,0)

#Background
turtle.bgcolor("#FFFFFF")
turtle.pencolor("#FF3300")
turtle.pensize(2)
turtle.hideturtle()
turtle.goto(0,0)

#Flower
for i in range(400):
    turtle.forward(200)
    turtle.right(300)
    turtle.backward(i)

turtle.done()