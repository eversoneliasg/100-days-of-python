# The range function is very helpful if you want to generate a range of numbers
for number in range(1, 11):  # 1 to 10
    print(number)
# You can fix a step size to the range
for num in range(1, 11, 3):
    print(num)

total = 0
for n in range(1, 101):
    total += n
print(total)
