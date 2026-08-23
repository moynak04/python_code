from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Functions
def move_forward():
    tim.forward(50)

def move_backward():
    tim.backward(50)

def turn_left():
    tim.left(90)

def turn_right():
    tim.right(90)

# Event listeners
screen.listen()

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.exitonclick()