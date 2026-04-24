def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication

add, sub, mul = calculate(10, 5)

print("Add:", add)
print("Sub:", sub)
print("Mul:", mul)