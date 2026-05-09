def makeAlbum(artistName, albumTitle):
    albumDic = {'name': artistName, 'album': albumTitle}
    return albumDic
   
    
while True:
    print("Please enter the artists name and album")
    print("Enter 'q' at anytime to quick")

    userArtist = input("Artist Name: ")
    if userArtist == 'q':
        break

    userAlbum = input("Album name: ")
    if userAlbum == 'q':
        break

    createdAlbum = makeAlbum(userArtist, userAlbum)
    print(createdAlbum)

