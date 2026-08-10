def calculate_average(numbers):
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]

    average = total / len(numbers)
    return average


numbers = [10, 20, 30, 40, 50]

result = calculate_average(numbers)

print("Numbers:", numbers)
print("Average:", result)