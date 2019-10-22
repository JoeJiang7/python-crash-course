magicians = ['joe', 'jiang', 'li']

def make_great(magicians):
    magician2 = []
    for magician in magicians:
        magicians1 = 'the Great ' + magician
        magician2.append(magicians1)
    return magician2
def show_magicians(magicians1):
    for magician in magicians1:
        print(magician)
currentmagician = make_great(magicians)
show_magicians(currentmagician)
