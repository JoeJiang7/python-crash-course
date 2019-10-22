import json
filename = 'username1.json'
def user_name_stored():
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = user_name_stored()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username1.json'
        with open(filename,'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back, " + username +"!")
greet_user()
