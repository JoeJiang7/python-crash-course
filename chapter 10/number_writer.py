import json

numbers = [1, 2, 3, 4, 5, 6]
filename = 'D:\\python crash course\\chapter 10\\numbers.json'
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)

