weight = int(input("ENTER YOUR WEIGHT IN KG:"))
height = int(input("ENTER YOUR HEIGHT IN METRES:"))
bmi = weight / (height ** 2)
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")