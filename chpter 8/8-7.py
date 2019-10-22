def make_album(singername , albumname):
    album = {'singer': singername, 'album': albumname}
    return album
album1 = make_album('jay' , 'xiaobang')
album2 = make_album('jiang' , 'gushi')
album3 = make_album('li' , 'hehe')
print(album1)
print(album2)
print(album3)