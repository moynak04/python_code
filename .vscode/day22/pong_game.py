from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.15
ball.dy = 0.15

left_score = 0
right_score = 0

score = Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 220)

def update_score():
    score.clear()
    score.write(
        f"{left_score}        {right_score}",
        align="center",
        font=("Courier", 30, "normal")
    )

def left_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 30)

def left_down():
    y = left_paddle.ycor()
    if y > -250:
        left_paddle.sety(y - 30)

def right_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 30)

def right_down():
    y = right_paddle.ycor()
    if y > -250:
        right_paddle.sety(y - 30)

screen.listen()

screen.onkeypress(left_up, "w")
screen.onkeypress(left_down, "s")

screen.onkeypress(right_up, "Up")
screen.onkeypress(right_down, "Down")

update_score()

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if (
        ball.xcor() > 330
        and ball.xcor() < 350
        and ball.distance(right_paddle) < 60
    ):
        ball.dx *= -1

    if (
        ball.xcor() < -330
        and ball.xcor() > -350
        and ball.distance(left_paddle) < 60
    ):
        ball.dx *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score += 1
        update_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score += 1
        update_score()

