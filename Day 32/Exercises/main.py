# Day 31 of Udemy's 100 Days of Python programming course
import smtplib
import datetime as dt
import random

my_email = "EMAIL HERE"
password = "PASSWORD HERE"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email, password = password)
#     connection.sendmail(
#         from_addr = my_email, 
#         to_addrs = "test.farish@outlook.com", 
#         msg = "Subject:Hello\n\nThis is the body of the email."
#         )

now = dt.datetime.now()
current_day = now.weekday()


if current_day == 1:
    with open("quotes.txt") as file:
        quotes = file.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "test.farish@outlook.com",
            msg = (f"Subject:Happy Monday!\n\n{random.choice(quotes)}.")
        )

