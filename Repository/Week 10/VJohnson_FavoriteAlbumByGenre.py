class Albums:
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
    # Displays the desired result when the object is printed
    def __str__(self):
        return f"{self.name} by {self.artist} is {self.genre}"

def buildList():
    # Items are added to the txt file in the following format
    # Album_Name Artist_Name Genre_Name
    with open("album.txt") as file:
        x = file.read()
    # Place the albums variable into the global scope so another function can access it
    global albums
    albums = []
    for z in x.split("\n"):
        if z:
            # The * Unpack operator takes the contents of the resultant list from z.split and feeds them into the Albums init method to create objects
            album = Albums(*z.split(","))
            albums.append(album)

def searchList(value):
    if value == "1":
        postPunkAlbums = [album for album in albums if album.genre == "Post_Punk"]
        for album in postPunkAlbums:
            print(album)
    elif value == "2":
        postMetalAlbums = [album for album in albums if album.genre == "Post_Metal"]
        for album in postMetalAlbums:
            print(album)
    elif value == "3":
        artRapAlbums = [album for album in albums if album.genre == "Art_Rap"]
        for album in artRapAlbums:
            print(album)

def isValid(value):
    validInput = ["1","2","3"]
    if value in validInput:
        return value
    else:
        return None

def getInput():
    while True:
        print('==== Make a Selection ====')
        print('    1. Post_Punk')
        print('    2. Post_Metal')
        print('    3. Art_Rap')
        tinput = isValid(input('    Select Genre -> '))
        if tinput is not None:
            return tinput
        else:
            print('You must make a valid selection.')

def main():
    buildList()
    t = getInput()
    searchList(t)

main()