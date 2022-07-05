from datetime import datetime
import random, smtplib, pandas

my_email = "EMAIL HERE"
password = "PASSWORD HERE"

data = pandas.read_csv("birthdays.csv")
birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

today = datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthdays:
    person = birthdays[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = my_email,
            msg = f"Subject:Happy Birthday!\n\n{letter}"
        )
