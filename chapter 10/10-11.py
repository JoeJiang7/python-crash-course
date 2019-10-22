import json

fav_number = input("What is your favourite number? ")
filename = 'favnumber.json'
with open(filename,'w') as file_object:

    json.dump(fav_number,file_object)