# Modifying Global Scope

enemies = 1

def increase_enemies():
  global enemies # This will take the global variable inside the function.
  # But this is confusing and can be the origin of many bugs.
  # Normally, people will advise you not to modify global scope.
  # We can, instead, return the current value.
  enemies = 2
  print(f"enemies inside function: {enemies}")

def increase():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")
increase()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159 # The convention to global constants is to use uppercase.
