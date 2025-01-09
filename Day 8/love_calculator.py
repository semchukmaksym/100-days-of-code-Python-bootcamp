def calculate_love_score(first_name, second_name):
    args = first_name + second_name
    to_check_true = "True".lower()
    to_check_love = "Love".lower()
    first_cypher = 0
    second_cypher = 0
    for letter in args:
        for n in to_check_true:
            if letter == n:
                first_cypher += 1
    for letter in args:
        for m in to_check_love:
            if letter == m:
                second_cypher += 1
    print(f"{first_cypher}{second_cypher}")
calculate_love_score("Kanye West", "Kim Kardashian")