from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(10)
tim.speed("fastest")

# List of directions
directions = [0, 90, 180, 270]

# Random colors
colors = ["red", "blue", "green", "yellow", "purple", "orange", "black"]

for _ in range(100):
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = Screen()
screen.exitonclick()