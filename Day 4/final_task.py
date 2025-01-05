import random

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

random_option = random.randint(0,2)
if user_choice < 0 or user_choice >= 3:
    print("You typed invalid number. You lose!")
else:
    print(f'''
    {option[user_choice]} \n
    Compute chose:\n
    {option[random_option]}
    ''')
    if user_choice == 0:
        if random_option == 0:
            print("It's draw")
        elif random_option == 1:
            print("You're lose")
        else:
            print("You win")
    elif user_choice == 1:
        if random_option == 0:
            print("You win")
        elif random_option == 1:
            print("It's draw")
        else:
            print("You're lose")
    else:
        if random_option == 0:
            print("You're lose")
        elif random_option == 1:
            print("You're win")
        else:
            print("It's draw")