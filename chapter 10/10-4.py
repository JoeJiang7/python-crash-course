filename = 'D:\python crash course\chapter 10\guest_book.txt'


with open(filename,'a') as file_object:
    message = ''
    while 'quit' not in message:
        message = input("please enter your name ")
        if message == 'quit':
            break
        print("hello! " + message)
        file_object.write(message+'\n')