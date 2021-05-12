# Type checking
# len(4837) is like passing a rock to a potato cutter
num_char = len(input("What is your name? "))
print(type(num_char))

# Type conversion (also know as casting)
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.") # Everything here is string

a = str(123)
print(type(a)) # <class 'str'>

b = float(123)
print(type(b)) # <class 'float'>

print(70 + float("100.5")) # This will output 170.5
print(str(70) + str(100)) # This will output 70100
