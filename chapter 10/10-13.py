import json

def check_user():
    filename = 'username2.json'
    with open(filename) as file_object:
        username = json.load(file_object)
    print("Hello! Are you " + username +"?")
    while True:
        flag = input('y/n ')
        if flag == 'y' or  flag =='n':
            break
    return flag

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
    with open(filename, 'w') as file_object:
        username = input("What is your name? ")
        print("We will remember your name when you come back " + username + "!")
        json.dump(username, file_object)
    return username

def greet_user():
    filename = 'username2.json'
    with open(filename) as file_object:
        username = json.load(file_object)
        print("Hello! " + username)
flag = check_user()
if flag == 'y':
    greet_user()
else:
    username = get_new_username()