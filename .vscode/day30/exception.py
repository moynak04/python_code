age = int(input("Enter your age: "))

if age < 18:
    raise Exception("You must be 18 or older.")

print("You can enter!")