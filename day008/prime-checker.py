#Write your code below this line 👇

def prime_checker(number):
    divisible_by = 0
    is_prime = True
    iterator = 1
    while iterator <= number and is_prime:
        if number % iterator == 0:
            divisible_by += 1
            iterator += 1
        else:
            iterator += 1
        if divisible_by > 2:
            is_prime = False
    if is_prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
