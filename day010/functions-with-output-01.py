# Functions with Outputs

# def my_function():
#   result = 3 * 2
#   return result

# result will replace the line of code that called the function
# we can atribute result to another variable

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"
    # whatever comes after the return is ignored

# print(format_name("everson", "oliveira"))
formated_string = format_name("eVeRsOn", "oLiVeIrA")
print(formated_string)
