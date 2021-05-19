# Functions:
# def my_function():
#   Do this
#   Then do this
#   Finally do this

# Later, to call a function, use my_function()

# We can also have a function with parameters:
# def my_function(something):
#   Do this with something
#   Then do this
#   Finally do this

# Later, to call a function, use my_function(something)
# When we pass a value, we are creating a variable called something that receives the value passed.
# If we pass 123, something = 123. Something is the parameter; 123 the argument.

def greet():
    print("Hello, Visitor!")
    print("How are you, Visitor?")
    print("I hope you are fine.")

greet()

def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How are you, {name}?")
    print("I hope you are fine.")

greet_with_name("Everson")
