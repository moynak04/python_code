# Python program using constants and global variables

# Constant (written in CAPITAL letters by convention)
PI = 3.14159

# Global variable
count = 0

def calculate_area(radius):
    global count
    count += 1
    
    area = PI * radius * radius
    print("Area of circle =", area)

# Main program
r = 5
calculate_area(r)

print("Function called", count, "time(s)")