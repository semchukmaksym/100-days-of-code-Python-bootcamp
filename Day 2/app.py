height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

weight_index = weight / height ** 2

print(int(weight_index))