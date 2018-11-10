import turtle as t

def rectangle(horizontal, vertical, color):
  t.pendown()
  t.pensize(1)
  t.color(color)
  t.begin_fill()
  for counter in range(1, 3):
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.right(90)
  t.end_fill()
  t.penup()