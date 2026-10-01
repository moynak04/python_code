import datetime

today = datetime.date.today()

birthday = datetime.date(int(input("Enter the year of your birthday: ")), int(input("Enter the month of your birthday: ")), int(input("Enter the day of your birthday: ")))

days_left = birthday - today

print(f"My birthday is in {days_left.days} days!")