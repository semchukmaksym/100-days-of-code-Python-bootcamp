year = int(input("Please enter year to check if its leap or not:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is the leap year")
        else:
            print("This is not leap year")
    else:
        print("This is leap year")
else:
    print("This is not leap year")