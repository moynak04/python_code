from turtle import Turtle, Screen

screen = Screen()
screen.title("Scoreboard")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

left_score = 0
right_score = 0

scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()

def update_score():
    scoreboard.clear()

    scoreboard.goto(-100, 200)
    scoreboard.write(
        f"PLAYER 1: {left_score}",
        align="center",
        font=("Arial", 24, "bold")
    )

    scoreboard.goto(100, 200)
    scoreboard.write(
        f"PLAYER 2: {right_score}",
        align="center",
        font=("Arial", 24, "bold")
    )

    screen.update()

def player1_score():
    global left_score
    left_score += 1
    update_score()

def player2_score():
    global right_score
    right_score += 1
    update_score()

def reset_score():
    global left_score, right_score
    left_score = 0
    right_score = 0
    update_score()

screen.listen()

screen.onkey(player1_score, "a")
screen.onkey(player2_score, "l")
screen.onkey(reset_score, "r")

instructions = Turtle()
instructions.color("white")
instructions.penup()
instructions.hideturtle()

instructions.goto(0, -150)
instructions.write(
    "PLAYER 1: Press A     PLAYER 2: Press L",
    align="center",
    font=("Arial", 16, "normal")
)

instructions.goto(0, -190)
instructions.write(
    "Press R to Reset Score",
    align="center",
    font=("Arial", 16, "normal")
)

update_score()

screen.mainloop()