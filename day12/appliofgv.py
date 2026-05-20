
PI = 3.14159

# Global variable
count = 0


def area(radius):
    global count   # accessing global variable
    count += 1
    return PI * radius * radius


def display():
    print("Program used", count, "times")

r1 = 5
r2 = 7

print("Area of circle 1 =", area(r1))
print("Area of circle 2 =", area(r2))

display()