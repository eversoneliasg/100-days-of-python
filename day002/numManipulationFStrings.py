print(8 / 3)
print(4 / 2)
print(int(8 / 3))

# Rouding number in Python is easy
print(round(8 / 3))

# We can go further and specify the amount of decimal places
print(round(8 / 3, 2))
# We can get the same output as above with print(round(2.66666, 2))

# Floor division: the type will be a integer, like if a cast is used
print(8 // 3)
result = 8 // 3
print(type(result))

# += -= *= /=
score = 1
score += 3
print(score)

# F strings: mixing strings and different data types
print("Your score is " + str(score)) # This is not convenient if you have a lot of variables
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
# Just place a f in front of the string.
