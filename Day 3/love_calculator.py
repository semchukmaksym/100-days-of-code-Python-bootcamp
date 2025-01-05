print("Welcome to the Love calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

combined_string = name1 + name2

true_count = combined_string.count("t") + combined_string.count("r") + combined_string.count("u") + combined_string.count("e")

love_count = combined_string.count("l") + combined_string.count("o") + combined_string.count("v") + combined_string.count("e")

score = int(str(true_count) + str(love_count))

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")

