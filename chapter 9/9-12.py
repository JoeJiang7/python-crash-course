import user
import privileges


user1 = privileges.Admin('joe', 'jiang')
user2 = user.User('joey','chow')
user2.greet_user()
user1.describe_user()
user1.privileges.show_privileges()