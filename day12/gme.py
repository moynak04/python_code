score = 0   # Global variable

def increase_score():
    global score
    score = score + 10
    print("You earned 10 points!")

def show_score():
    print("Current Score:", score)

# Main Program
print("=== Simple Game ===")

increase_score()
show_score()

increase_score()
show_score()