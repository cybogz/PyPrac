def makeAlbum(artistName, albumTitle, tracks = ''):
    albumDic = {'name': artistName, 'album': albumTitle}

    if tracks:
        albumDic['tracks'] = tracks
    return albumDic

createAlbum = makeAlbum("megadeth", "rust in peace")
print(createAlbum)

createAlbum = makeAlbum("tool", "lateralus", 9)
print(createAlbum)

