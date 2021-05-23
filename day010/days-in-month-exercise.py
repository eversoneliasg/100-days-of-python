def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(chosen_year, chosen_month):
  if month > 12 or month < 1:
      return "Invalid inputs."
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(chosen_year) and chosen_month == 2: # We don't need to say is_leap(chosen_year) == True
      return 29
  else:
      return month_days[chosen_month - 1] # Remember that lists start at index 0

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
