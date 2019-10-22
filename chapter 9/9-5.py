class User():
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("User 's name is " + self.firstname + self.lastname)

    def greet_user(self):
        print("Hello! " + self.firstname + self.lastname)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('joe', 'jiang')
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
print(user1.login_attempts)