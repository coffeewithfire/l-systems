import turtle

axiom = 'F+F+F+F'
mod = {'+': '+',
       '-': '-',
       'f': 'f',
       'F': 'F+F-f-F+F'}

for _ in range(3):
    axiom = axiom.translate(str.maketrans(mod))
    print(axiom)

turtle.penup()
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
turtle.setposition(-380, 300)
turtle.pendown()
turtle.pensize(1.5)

for c in axiom:
    if c == 'F' or c == 'f':
        turtle.forward(20)
    elif c == '-':
        turtle.left(45)
        turtle.forward(8)
        turtle.left(45)
    elif c == '+':
        turtle.right(45)
        turtle.forward(8)
        turtle.right(45)

turtle.update()
turtle.done()