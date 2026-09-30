import smtplib

my_email = "moynaks_25isai@gmail.com"
password = "acharya@123"

connection = smtplib.SMTP("smtp.gmail.com", 587)

connection.starttls()

connection.login(my_email, password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="recipient@gmail.com",
    msg="Subject: Test Email\n\nHello! This email was sent using Python."
)

connection.quit()