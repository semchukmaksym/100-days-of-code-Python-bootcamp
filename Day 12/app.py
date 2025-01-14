import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")

attempts = 0
secret_number = random.randint(1,100)

if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number")
    while attempts > 0:
        user_choise = int(input("Choose your number"))
        if user_choise > secret_number:
            attempts -= 1
            print("Too high")
            print(f"You have {attempts} attempts remaining to guess the number")
        elif user_choise < secret_number:
            attempts -=1
            print("Too low")
            print(f"You have {attempts} attempts remaining to guess the number")
        if user_choise == secret_number:
            print("You win")
            break
    if attempts == 0:
        print("You are out of attempts. Please play one more game")
elif difficulty == "hard":

    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number")

    while attempts > 0:
        user_choise = int(input("Choose your number"))
        if user_choise > secret_number:
            attempts -= 1
            print("Too high")
            print(f"You have {attempts} attempts remaining to guess the number")
        elif user_choise < secret_number:
            attempts -=1
            print("Too low")
            print(f"You have {attempts} attempts remaining to guess the number")
        if user_choise == secret_number:
            print("You win")
            break
    if attempts == 0:
        print("You are out of attempts. Please play one more game")