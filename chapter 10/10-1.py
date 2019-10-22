filename = 'D:\python crash course\chapter 10\learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print('_________"1"___________')
    print(contents)

with open(filename) as file_object:
    print('_________"2"___________')
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
    print('_________"3"___________')
    for line in lines:
        print(line.rstrip())
