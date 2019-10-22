import json
filename = 'favnumber2.json'
def stored_number():
    try:
        with open(filename) as file_object:
            number = json.load(file_object)
        return number
    except FileNotFoundError:
        return None

def fav_number():
    with open(filename) as file_object:
        number = json.load(file_object)
        return number

def new_fav_number():
    number = stored_number()
    with open(filename,'w') as file_object:
        if number:
            print("I know your favourite number! It's " + number)
        else:
            number = input("What is your favourite number? ")
            json.dump(number,file_object)

new_fav_number()
