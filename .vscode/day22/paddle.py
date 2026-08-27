from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Paddle")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def move_up():
    new_y = paddle.ycor() + 20
    if new_y < 250:
        paddle.sety(new_y)

def move_down():
    new_y = paddle.ycor() - 20
    if new_y > -250:
        paddle.sety(new_y)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.mainloop()