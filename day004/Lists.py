# Lists are data structures
# They are simple to create: fruits = [item1, item2]
# The itens can be of any type

states_of_brazil = ["Minas Gerais", "Pernambuco", "Rio Grande do Sul"]

# Lists can also have a order, which is determined by ther order of the itens
print(states_of_brazil[0])

# The position is determined by the distance of the item from the beginning of the list
print(states_of_brazil[-1]) # The last item of the list. We can have negative indexes

# We can replace the itens
states_of_brazil[0] = "Espirito Santo"
print(states_of_brazil[0])

# It is possible to add a new item
states_of_brazil.append("Mato Grosso")
print(states_of_brazil)

# Adding more than one item
states_of_brazil.extend(["Acre", "Ceara"])
print(states_of_brazil)

# We can have a list of lists, what is called nested lists
