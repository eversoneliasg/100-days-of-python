class Nothing:
    pass


class User:

    def __init__(self, user_id, username):  # It is common to see the name of the parameter being
        # the same of the attribute. The constructor wit parameters demands arguments everytime we create an object.
        print("new user being created...")  # This will be printed everytime we create an user
        self.id = user_id
        self.username = username
        self.followers = 0  # Default value, so we won't need to pass it as a parameter
        self.following = 0

    def follow(self, user):  # A method always need to have a self parameter.
        user.followers += 1
        self.following += 1


class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2


user_1 = User("001", "Angela")
# user_1.id = "001"  # Python allows us to create attributes like this. But it increases the chance of error
# user_1.username = "angela"
print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User("002", "Bane")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# my_car = Car(5)  # This is the same as my_car.seats = 5, but it make it quicker
# print(my_car.seats)

# my_car.enter_race_mode()
# print(my_car.seats)
