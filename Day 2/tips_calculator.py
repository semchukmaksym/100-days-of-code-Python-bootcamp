print("Welcome to the tip calculator\n")

total_bill = float(input("What was the total bill?\n"))

tip_persentage = int(input("What persentage tip would you like to give? 10,12, or 15?\n")) /100

persons = int(input("How many people to plit the bill?\n"))

tips = (total_bill * tip_persentage) / persons

each_person = round(total_bill / persons + tips, 2)

result = print(f"Each person should pay: {each_person}")