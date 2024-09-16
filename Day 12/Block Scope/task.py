# There is no block scope in python

game_level = 10
enemies = ["skeleton", "zombie", "Alien"]

def create_enemy():
    new_enymy = ""
    if game_level < 5:
        new_enymy = enemies[0]
    print(new_enymy)

create_enemy()