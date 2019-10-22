message1 = "Please enter a singer's name "
message2 = "Please enter his album's name "
def make_album(singername , albumname):
    album = {'singer': singername, 'album': albumname}
    return album
Active = True
while Active:
    singername = input(message1)
    albumname = input(message2)
    if singername == 'quit' or albumname == 'quit':
        break
    singeralbum = make_album(singername, albumname)
    print(singeralbum)