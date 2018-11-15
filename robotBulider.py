import turtle as t

def rectangle(horizontal, vertical, color):
  t.pendown()
  t.pensize(1)
  t.color(color)
  t.begin_fill()
  for counter in range(1, 3): #this block draws the rectangle
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.right(90)
  t.end_fill()
  t.penup()
  t.speed('slow')
  t.bgcolor('Dodger blue')

  #feet
  t.goto(-100, -150)
  rectangle(50, 20, 'blue')