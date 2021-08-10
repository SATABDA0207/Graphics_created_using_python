import turtle
c = input("Press:\n1. To see square\n2. To see circle\nEnter the choice: ")

for i in range(6):
    for colours in ["red", "magenta", "blue", "yellow", "green", "white"]:
        if c == "1":
            window = turtle.Screen()
            window.title("Abstract shape")
            turtle.bgcolor("black")
            turtle.pensize(2)
            turtle.speed(10.49)
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(10)
        if c == "2":
            window = turtle.Screen()
            window.title("Abstract shape")
            turtle.bgcolor("black")
            turtle.pensize(2)
            turtle.speed(10.49)
            turtle.color(colours)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.left(10)

turtle.hideturtle()