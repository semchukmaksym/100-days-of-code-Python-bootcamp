age = input("How old are you?")

remain = 90 - int(age)
day = remain*365
week = remain*52
month = remain*12

output = f"You have {day} days, {week} weeks, and {month} month left"
print(output)