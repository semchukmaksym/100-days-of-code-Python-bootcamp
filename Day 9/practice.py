nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Djon"]
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamsburg"],
        "total_visits" : 5,
    }
}

print(travel_log["Germany"]["total_visits"])