# import smtplib

# ---------------------------------WORKING WITH SMTP----------------------------------
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=email_to_send,
#         msg="Subject:Hello\n\n This is the body of my email.")
#     connection.close()
#
# --------------------------WORKING WITH DATETIME MODULE------------------------------------

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# data_of_birth = dt.datetime(year=1999, month=11, day=11, hour=11)

# ---------------------------------------PRACTICE--------------------------------------------

from password import *

my_email = EMAIL
password = PASSWORD
email_to_send = TO_EMAIL

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_to_send,
                msg=f"Subject:Monday motivation\n\n{quote}"
            )