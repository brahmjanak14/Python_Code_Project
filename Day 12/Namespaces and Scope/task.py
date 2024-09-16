enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# here not define global variable
# print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()

game()
print(player_health)

