filename = 'D:\python crash course\chapter 10\learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        line = line.replace('Python', 'C')
        print(line)