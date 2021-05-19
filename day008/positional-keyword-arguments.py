# Positional vs. Keyword arguments

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

# Positional Arguments:
greet_with("Everon", "Belo Horizonte")
# The first argument is assigned to the first parameter; the second argument, to the second parameter; and so on...
# This is the default way to declare and call functions.

# Keyword arguments:
# We will be able to change the order of the arguments and it won't affect the function.
greet_with(location = "New Mexico", name = "Mary")
