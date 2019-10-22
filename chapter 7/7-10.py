message = "If you could visit one place in the world, where would you go? "
place = message
places = []
while place != "quit":
    place = input(message)
    places.append(place)
for i in places:
    print("Dearming placese: " + i)