from turtle import Screen, Turtle
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("green")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Food
food = Turtle("circle")
food.color("red")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Scoreboard
score = 0
high_score = 0

try:
    with open("data.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, 260)

def update_score():
    scoreboard.clear()
    scoreboard.write(
        f"Score: {score}    High Score: {high_score}",
        align="center",
        font=("Arial", 18, "bold")
    )

update_score()

# Movement
direction = "Up"

def go_up():
    global direction
    if direction != "Down":
        direction = "Up"

def go_down():
    global direction
    if direction != "Up":
        direction = "Down"

def go_left():
    global direction
    if direction != "Right":
        direction = "Left"

def go_right():
    global direction
    if direction != "Left":
        direction = "Right"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Game
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)

    if direction == "Up":
        segments[0].sety(segments[0].ycor() + 20)

    if direction == "Down":
        segments[0].sety(segments[0].ycor() - 20)

    if direction == "Left":
        segments[0].setx(segments[0].xcor() - 20)

    if direction == "Right":
        segments[0].setx(segments[0].xcor() + 20)

    # Food collision
    if segments[0].distance(food) < 15:
        food.goto(
            random.randint(-280, 280),
            random.randint(-280, 280)
        )

        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 1

        if score > high_score:
            high_score = score

        update_score()

    # Wall collision
    if (
        segments[0].xcor() > 290
        or segments[0].xcor() < -290
        or segments[0].ycor() > 290
        or segments[0].ycor() < -290
    ):
        game_is_on = False

    # Self collision
    for segment in segments[1:]:
        if segments[0].distance(segment) < 10:
            game_is_on = False

# Save high score
with open("data.txt", "w") as file:
    file.write(str(high_score))

scoreboard.goto(0, 0)
scoreboard.write(
    f"GAME OVER\nScore: {score}\nHigh Score: {high_score}",
    align="center",
    font=("Arial", 20, "bold")
)

screen.mainloop()