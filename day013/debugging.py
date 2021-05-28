############DEBUGGING#####################

# # Describe Problem
# # Below, we have a function that
# # loops in a range and, when i reachs
# # 20, it will print "You got it".
# def my_function():
#   for i in range(1, 20): # The problem is here. 20 is not included in the range.
#     if i == 20: # i never reachs 20. Our assumption is wrong.
#       print("You got it")
# my_function()

# Corrected:
def my_function():
  for i in range(1, 21): # The problem is here. 20 is not included in the range.
    if i == 20: # i never reachs 20. Our assumption is wrong.
      print("You got it")
my_function()


# # Reproduce the Bug: sometimes, the code below will give an error.
# # So, we must try to reproduce it and, then, change the code.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # The documentaion says that 1 and 6 are included.
# print(dice_imgs[dice_num])

# Corrected:
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])


# # Play Computer
# # If we input 1994, in the code below, there will be not output.
# # It's because 1994 isn't in any of the if's.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Corrected:
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: # This is enough to correct the code.
  print("You are a Gen Z.")


# # Fix the Errors
# In the code below, the editor will aid us telling the identation error.
# Also, the error will be shown at the terminal. We can copy it
# and search on Google, for example.
# However, the editor won't show all errors.
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# Corrected:
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# #Print is Your Friend
# # The code below will return 0, even when we input numbers bigger than 0.
# # We can try to see what happens to our variables with the print function.
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# # Print will help us to identify the error on the line above.
# total_words = pages * word_per_page
# print(total_words)

# Corrected:
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages) # We can take it out, after we find out what the error was.
word_per_page = int(input("Number of words per page: "))
print(word_per_page) # We can take it out, after we find out what the error was.
total_words = pages * word_per_page # The error was here.
print(total_words)

# #Use a Debugger
# # The function below should take the list and multiply each item for 2.
# # We can take the code to Python tutor and analyze it line by line: http://www.pythontutor.com/
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Corrected:
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # We changed the identation of this line.
  print(b_list)

mutate([1,2,3,5,8,13])