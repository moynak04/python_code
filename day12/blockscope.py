x = 10   # Global variable

if x > 5:
    y = 20   
    print("Inside block:")
    print("x =", x)
    print("y =", y)

print("\nOutside block:")
print("x =", x)
print("y =", y)   