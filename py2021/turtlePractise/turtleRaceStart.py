from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win race? Enter color: ")
colors = [
"red",
  "orange",
  "yellow",
  "green",
  "blue",
  "purple"
]
y_positions = []

for turtle_index in range(0,6):
  tim = Turtle(shape = "turtle")
  timp.penup()
  tim.goto(x=-230, y=-100)
  
 
screen.exitonclick()




