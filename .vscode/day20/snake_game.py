from turtle import Screen, Turtle
from random import randint
import time

# -------------------- CONSTANTS --------------------

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# -------------------- SNAKE --------------------

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move each segment to the position of the segment in front
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()

            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# -------------------- FOOD --------------------

class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)

        self.goto(random_x, random_y)


# -------------------- SCOREBOARD --------------------

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Courier", 24, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=("Courier", 30, "bold")
        )


# -------------------- SCREEN SETUP --------------------

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# -------------------- CREATE OBJECTS --------------------

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# -------------------- KEYBOARD CONTROLS --------------------

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# -------------------- GAME LOOP --------------------

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # -------------------- COLLISION WITH FOOD --------------------

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # -------------------- COLLISION WITH WALL --------------------

    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()

    # -------------------- COLLISION WITH TAIL --------------------

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


# -------------------- KEEP WINDOW OPEN --------------------

screen.exitonclick()