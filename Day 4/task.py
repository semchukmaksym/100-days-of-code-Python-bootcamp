import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 Option

print(f"{random.choice(friends)} will pay the bill")

# 2 Option

who_will_pay = random.randint(0,4)

print(f"{friends[who_will_pay]} will pay the bill")