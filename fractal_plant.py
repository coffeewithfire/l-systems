import turtle
import random

axiom = 'X'

ts = {'X': 'F-[[X]+X]+F[+FX]-X',
      'F': 'FF'}

for _ in range(6):
    axiom = axiom.translate(str.maketrans(ts))
print(axiom)

turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -400)
turtle.setheading(random.randint(80, 110))
turtle.pendown()

ang = 0
stk = []

for c in axiom:
    if c == 'F':
        turtle.forward(5)
    elif c == '+':
        turtle.right(random.randint(0, 30))
    elif c == '-':
        turtle.left(random.randint(0, 30))
    elif c == '[':
        x = turtle.xcor()
        y = turtle.ycor()
        ang = turtle.heading()
        stk.append((x, y, ang))
    elif c == ']':
        x, y, ang = stk.pop()
        turtle.penup()
        turtle.setposition(x, y)
        turtle.setheading(ang)
        turtle.pendown()

turtle.update()
turtle.done()