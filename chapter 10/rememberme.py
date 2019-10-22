import json

#如果以前存储了用户名，就加载他
def greet_user():
    filename = 'D:\\python crash course\\chapter 10\\username.json'
    try:
        with open(filename) as file_object:
            user_name = json.load(file_object)
    except FileNotFoundError:
        user_name = input('Please enter your name: ')
        with open(filename,'w') as file_object:
            json.dump(user_name,file_object)
            print("We will remember your name when you come back, " + user_name + "!")
    else:
        print("Welcome back, " + user_name + "!")
greet_user()