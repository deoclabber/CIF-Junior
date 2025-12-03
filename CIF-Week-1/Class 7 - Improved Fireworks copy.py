import turtle
from random import randint

#Setting up turtle
turtle.speed(0)
turtle.delay(0)
turtle.shape("arrow")

#Background
turtle.bgcolor("#03010e")
turtle.hideturtle()

#Grass
turtle.penup()
turtle.fillcolor("#2F5413")
turtle.pencolor("#2F5413")
turtle.goto(-1000, -500)

turtle.pendown()
turtle.begin_fill()

turtle.forward(2000)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(2000)
turtle.left(90)
turtle.forward(200)
turtle.left(90)

turtle.end_fill()
turtle.penup()

#Set position
turtle.goto(100, -250)
turtle.seth(0)

#Firework box
turtle.pendown()

turtle.fillcolor("red")
turtle.pencolor("red")

turtle.begin_fill()

turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)

turtle.end_fill()

#Stars
turtle.penup()

for i in range(randint(50, 70)):
    
    #Random x and y coordinates
    turtle.goto(randint(-1000, 1000), randint(50, 500))

    turtle.pendown()
    
    turtle.speed(0)
    turtle.color("white")
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.shapesize(0.1)
    turtle.shape("arrow")

    turtle.begin_fill()

    turtle.right(145)
    turtle.forward(25)
    turtle.right(145)
    turtle.forward(25)
    turtle.right(145)
    turtle.forward(25)
    turtle.right(145)
    turtle.forward(25)

    turtle.end_fill()

    turtle.penup()

#Set position
turtle.seth(0)
turtle.goto(100, -250)
turtle.forward(50)
turtle.left(90)

turtle.pendown()

#Firework
turtle.showturtle()
turtle.speed(0)
turtle.color("#FD4800")
turtle.pencolor("#FD4800")
turtle.pensize(3)
turtle.shapesize(1.5)
turtle.shape("circle")

for i in range(30):
    turtle.forward(18)
    turtle.left(1)

turtle.goto(15, 270)

turtlelist = [] * 23
turtle.color("#FD0000")
turtle.pencolor("#FD0000")
turtle.pensize(3)
turtle.shapesize(2)
turtle.speed(10)

#Clone turtles
for i in range(23):
    turtlelist.append(turtle.clone())
    turtlelist[i].right(i * 15.652173913)
    turtlelist[i].hideturtle()

#Forward turtles
for j in range(50):
    for i in range(23):
        turtlelist[i].forward(4)
        turtlelist[i].right(1)

turtlelist = [] * 23
turtle.color("#FD4800")
turtle.pencolor("#FD4800")
turtle.pensize(2.5)
turtle.shapesize(2)
turtle.speed(9)

#Clone turtle
for i in range(23):
    turtlelist.append(turtle.clone())
    turtlelist[i].right(7.25)
    turtlelist[i].right(i * 15.652173913)
    turtlelist[i].hideturtle()

#Forward turtles
for j in range(45):
    for i in range(23):
        turtlelist[i].forward(4)    

turtlelist = [] * 15
turtle.color("#FDBE00")
turtle.pencolor("#FDBE00")
turtle.pensize(2)
turtle.shapesize(2)

#Clone turtle
for i in range(15):
    turtlelist.append(turtle.clone())
    turtlelist[i].right(3)
    turtlelist[i].right(i * 24)
    turtlelist[i].hideturtle()

#Forward turtles
for j in range(40):
    for i in range(15):
        turtlelist[i].forward(4) 

turtle2 = turtle.clone()

turtle2.penup()
turtle2.goto(100, -250)
turtle2.seth(0)
turtle2.forward(50)
turtle2.left(90)
turtle2.pendown()

# Firework
turtle2.showturtle()
turtle2.speed(0)
turtle2.color("#00ECFD")
turtle2.pencolor("#00ECFD")
turtle2.pensize(3)
turtle2.shapesize(1.5)
turtle2.shape("circle")

for i in range(30):
    turtle2.forward(18)
    turtle2.right(1.5)

turtlelist = [] 
turtle2.color("#00ECFD")
turtle2.pencolor("#00ECFD")
turtle2.pensize(3)
turtle2.shapesize(2)
turtle2.speed(10)

# Clone turtles using turtle2
for i in range(23):
    turtlelist.append(turtle2.clone())
    turtlelist[i].right(i * 15.652173913)
    turtlelist[i].hideturtle()

# Forward turtles
for j in range(60):
    for i in range(23):
        turtlelist[i].forward(4)
        turtlelist[i].right(3)

turtlelist = []
turtle2.color("#0072FD")
turtle2.pencolor("#0072FD")
turtle2.pensize(2.5)
turtle2.shapesize(2)
turtle2.speed(9)

# Clone turtles using turtle2
for i in range(23):
    turtlelist.append(turtle2.clone())
    turtlelist[i].right(7.25)
    turtlelist[i].right(i * 15.652173913)
    turtlelist[i].hideturtle()

# Forward turtles
for j in range(55):
    for i in range(23):
        turtlelist[i].forward(4)
        turtlelist[i].right(1)
        
turtlelist = []
turtle2.color("#001EFD")
turtle2.pencolor("#001EFD")
turtle2.pensize(2)
turtle2.shapesize(2)

# Clone turtles using turtle2
for i in range(15):
    turtlelist.append(turtle2.clone())
    turtlelist[i].right(3)
    turtlelist[i].right(i * 24)
    turtlelist[i].hideturtle()

# Forward turtles
for j in range(50):
    for i in range(15):
        turtlelist[i].forward(4)

turtle.done()