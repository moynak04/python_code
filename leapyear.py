def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "Leap year"
    else:
        return "Not a leap year"


# Taking input
year = int(input("Enter a year: "))

# Function call
result = is_leap_year(year)
print(result)