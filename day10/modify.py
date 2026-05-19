count = 10   # Global variable

def change_value():
    global count   # Access the global variable
    count = count + 5

print("Before function call:", count)

change_value()

print("After function call:", count)