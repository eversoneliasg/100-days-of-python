# Scope!
# Remember the example of one apple tree planted inside a property and another planted by the sidewalk.

enemies = 1

def increase_enemies():
  enemies = 2 # This will create a different variable to be printed inside the function.
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope.

def drink_potion():
    potion_strength = 2 # Local Scope.
    print(potion_strength)

drink_potion()
# print(potion_strength) ERROR!
# The potion_strength is inside the scope of the function.

# Global scope.

player_health = 10 # Avaliable anywhere.

def drink_healing_potion():
    potion_strength = 2
    print(player_health)

drink_healing_potion()

# Whenever we give a name to anything, we have to be aware of the location.
# We create variables ate the first time we give it a name and value.
# We create functions with def.

# There is no block scope in Python.

game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_strong_enemy = enemies[2] # This variable only will be avaliable inside the function
    print(new_strong_enemy)

if game_level < 5:
    new_enemy = enemies[0] # When inside a if, for or while, the variable won't be considered inside a local scope

print(new_enemy)
