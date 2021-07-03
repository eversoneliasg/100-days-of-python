from prettytable import PrettyTable  # You can right-click over prettytable and go to the implementation.
# You can access the documentation on the pypi.org.

another_variable = 12

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
