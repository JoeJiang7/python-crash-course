def word_count(filename):
    '''计算一个文件大概包含多少单词'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + 'do not exists.'
        print(msg)
    else:
        words = contents.split()
        newwords = len(words)
        print('The file ' + filename + ' has about ' + str(newwords)+ ' words.')
        number = words.count('the')
        number2 = contents.count('the')
        print('The number of the word "the" in this file is ' + str(number))
        print(number2)
filename = 'D:\\python crash course\\chapter 10\\2542.txt'
word_count(filename)