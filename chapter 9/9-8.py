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


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin1 = Admin('joe', 'jiang')
admin1.greet_user()
admin1.privileges.show_privileges()
