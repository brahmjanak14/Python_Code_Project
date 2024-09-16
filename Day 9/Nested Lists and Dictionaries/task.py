capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary

travel_log = {
    "France" : ["Paris", "Little", "Dijon"],
    "Germany": ["stuttgart", "Berlin"]
}

# print list
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C","D"]]

# print(nested_list[2][1])

travel_log = {
    "France":{
        "cities_visited":["Paris", "Lille", "Dijoin"],
        "total_visits":12,
    },
    "Germany":{
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
}

print(travel_log["Germany"]["cities_visited"][2])