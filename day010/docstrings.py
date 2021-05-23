# Docstrings

# Docstrings are, basically, a way of creating little bits of documentation as we are coding along functions or codeblocks
# Docstrings have the layout below:

def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

# We can use docstrings as commentary:
"""
But it
is not
advisable.
"""

# The format below is more adequate:

# This is
# better, because
# avoids confusion.
# Hotkey: CTRL + /
