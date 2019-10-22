class User():
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def describe_user(self):
        print("User 's name is " + self.firstname + self.lastname)

    def greet_user(self):
        print("Hello! " + self.firstname + self.lastname)


user1 = User('joe', 'jiang')
user2 = User('jay', 'chou')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()