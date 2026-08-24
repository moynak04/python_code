from turtle import Turtle, Screen

# Create screen
screen = Screen()
screen.title("Etch-A-Sketch")
screen.bgcolor("white")

# Create turtle
t = Turtle()
t.shape("turtle")
t.color("black")
t.speed("fastest")

# Movement functions
def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

def exit_program():
    screen.bye()

# Keyboard controls
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.onkey(exit_program, "x")

# Keep window open
screen.mainloop()