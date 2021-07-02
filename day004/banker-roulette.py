# Who's Paying The Bill? Banker Roulette
# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# Don't use the choice() function
# Split string method

import random
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ") # Split the spring according to some sort of divider
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
length = len(names)
rand = random.randint(0, length - 1)
person_who_will_pay = names[rand]
print(f"{person_who_will_pay} is going to buy the meal today!")
