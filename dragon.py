import turtle

axiom = 'FX'

ts = {'X': 'X+YF+',
      'Y': '-FX-Y'}

for _ in range(16):
    axiom = axiom.translate(str.maketrans(ts))

turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)
turtle.penup()
turtle.setposition(-100, -150)
turtle.pendown()

for c in axiom:
    if c == 'F':
        turtle.forward(2)
    elif c == '+':
        turtle.right(90)
    elif c == '-':
        turtle.left(90)

turtle.update()
turtle.done()