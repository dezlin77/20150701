import turtle as t
import random

tim = t.Turtle()

colors = [
"CornflowerBlue",
"DarkOrchid",
"IndianRed", 
"DeepSkyBlue",
"LightSeaGreen",
"wheat",
"SlateGray",
"SeaGreen"
]

directions = [30, 90, 120, 150]

tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
  tim.color(random.choice(colors))
  tim.forward(30)
  tim.setheading(random.choice(directions))


