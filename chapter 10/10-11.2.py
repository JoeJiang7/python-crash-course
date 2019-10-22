import json
filename = 'favnumber.json'
def favourite_number():
    with open(filename) as file_object:
        favouritenumber = json.load(file_object)
    return  favouritenumber

number = favourite_number()
print(number)