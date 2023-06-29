class User:
    def __init__(self, first, last, age):
       # print('new user being created')
        self.name = first
        self.last = last
        self.age = age

user1 = User('Joe', 'Smith', 68)
user2 = User('Blanca', 'Lopez', 41)
print(user1.name, user1.last, user1.age)    # Joe Smith 68
print(user2.name, user2.last, user2.age)    # Blanca Lopez 41
user3 = User()
print(user3)   # AttributeError: 'User' object has no attribute 'name'
    