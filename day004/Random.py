import random

# Random integer numbers
random_integer = random.randint(1,10)
print(random_integer)

# Random floating point number between 0.00000000 - 0.9999999...
random_float = random.random()
# How can we expand the range? Multiplying the random float: random_float * 5
random_float *= 5
print(random_float)

love_score = random.randint(1 , 100)
print(f"Your love score is {love_score}")
