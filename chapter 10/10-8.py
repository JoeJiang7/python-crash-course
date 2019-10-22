filename1 = 'D:\python crash course\chapter 10\cats.txt'
filename2 = 'D:\python crash course\chapter 10\dos.txt'
try:
    with open(filename1) as file_object1:
        contents = file_object1.read()
        print(contents)

    with open(filename2) as file_object2:
        contents = file_object2.read()
        print(contents)
except FileNotFoundError:
    pass