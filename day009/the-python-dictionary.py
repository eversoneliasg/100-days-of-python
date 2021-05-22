# The Python Dictionary

# Normally, dictionaries wil have the layout below:
programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
123: "A number",
}

# Dictionaries are accessed with their keys.
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Empty dictionary
empty_dictionary = {}

# Edit an item in a dictionary (similar to adding)
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary: # This will just give me the keys
    print(thing)
for key in programming_dictionary: # This will give me the key and the definition
    print(key)
    print(programming_dictionary[key])

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
