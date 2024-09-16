import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


# 1 Option
print(random.choice(friends))

# 2nd Option
length = len(friends)
random_index = random.randint(0, length- 1)
print(friends[random_index])
print(len(friends))