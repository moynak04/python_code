from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fastest")
tim.pensize(2)

colors = ["red", "blue", "green", "purple", "orange", "pink", "cyan", "yellow"]

for _ in range(100):
    tim.color(random.choice(colors))
    tim.circle(100)
    tim.setheading(tim.heading() + 10)

screen = Screen()
screen.exitonclick()