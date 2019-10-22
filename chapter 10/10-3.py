filename = 'D:\python crash course\chapter 10\guest.txt'


message = input("please enter your name ")
with open(filename,'w') as file_object:
    file_object.write(message)