print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

total = 0
if size == "S":
    total += 15
elif size == "M":
    total+= 20
elif size == "L":
    total +=25

if add_pepperoni == "Y":
    if size == "S":
        total += 2
    elif size == "M":
        total += 3
    elif size == "L":
        total += 3

if extra_cheese == "Y":
    total +=1

print(f"Your total bill is: ${total}")