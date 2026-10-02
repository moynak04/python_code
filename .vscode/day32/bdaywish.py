import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"

# Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays.csv
data = pandas.read_csv("C:/python_codes/.vscode/day32/birthdays.csv")

# Create dictionary of birthdays
birthdays_dict = {
    (row["month"], row["day"]): row
    for (index, row) in data.iterrows()
}

# Check if today is someone's birthday
if today_tuple in birthdays_dict:

    birthday_person = birthdays_dict[today_tuple]

    # Choose a random letter
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()

    # Replace [NAME] with actual name
    contents = contents.replace("[NAME]", birthday_person["name"])

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )