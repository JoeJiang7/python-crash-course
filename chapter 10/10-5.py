filename = 'D:\\python crash course\\chapter 10\\reasons.txt'


with open(filename,'a') as file_object:
    file_object.seek(0)
    file_object.truncate()
    while True:
        reason = input("Why do you like programming? ")
        if reason == 'quit':
            break
        elif reason == 'cls':
            file_object.truncate()
        else:
            file_object.write("Because " + reason + '\n')