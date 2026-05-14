# Python program to demonstrate block scope

x = 100   # Global variable

def test():
    x = 50   # Local variable inside function
    print("Inside function before block:", x)

    if True:
        x = 25   # Same function scope variable modified
        y = 10   # Created inside if block

        print("Inside if block:")
        print("x =", x)
        print("y =", y)

    print("Outside if block but inside function:")
    print("x =", x)
    print("y =", y)   # Accessible because Python has no block scope for if/loop

test()

print("Outside function:")
print("Global x =", x)

# print(y)  # Error: y is not accessible outside function