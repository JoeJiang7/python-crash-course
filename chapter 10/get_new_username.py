import json

def get_stored_username():
    filename = 'username2.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    filename = 'username2.json'
    with open(filename,'w') as file_object:
        username = input("What is your name? ")
        json.dump(username,file_object)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back " + username +"!")
    else:
        username = get_new_username()
        print("We will remember your name whrn you come back " + username + "!")
greet_user()