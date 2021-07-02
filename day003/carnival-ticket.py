print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
# Watch for the identation!
if height >= 120:
  print("You can ride the rollercoaster!")
# We can check for another conditions wit a nested if/else statement or elif
# We will check how much a person will pay, according to his/her age and if they want a photo
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55: # Midlife crisis special prize.
    print("Everything is going to be OK. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Type Y or N: ")
  if wants_photo == "Y":
    # Add $3 to their bill
    bill += 3
  
  print(f"Your final bill is ${bill}.")

else:
  print("Sorry, you have to grow taller before you can ride.")

# > greater than
# < less than
# >= greater than or equal to
# <= lesser than or equal to
# == equal to
# != not equal to
