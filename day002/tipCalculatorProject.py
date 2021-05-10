# The tip calculator project

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Greeting
print("Dear visitor, welcome to the tip calculator!")
# Getting the total bill
total_bill = input("What was the total bill? $ ")
# Asking for tip percentage
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
# Asking for how many people will split the bill
people_splitting = input("How many people to split the bill? ")
# Output
total_bill_float = float(total_bill)
tip_percentage_float = 1 + int(tip_percentage) / 100
people_splitting_integer = int(people_splitting)
pay_for_person = round(total_bill_float * tip_percentage_float / people_splitting_integer, 2)
print(f"Each person should pay: {pay_for_person}")
