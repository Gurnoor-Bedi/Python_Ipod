import random
artist_songs={}
while len(artist_songs)<4:
  artist=input("Enter an artist or press enter to finish.")
  if not artist:
    break
  songs=[]
  while len(songs)<3:
    song=input("Enter a song by {} or press enter to finish: ".format(artist))
    if not song:
      break
    songs.append(song)
  artist_songs[artist] =songs

sort_songs=sorted([(artist,song) for artist,songs in artist_songs.items() for song in songs])
print("Sorted playlist: ")
for artist,song in sort_songs:
  print("{}-{}".format(artist,song))

print("Random playlist: ")
random_songs=random.sample(sort_songs, len(sort_songs))
for artist,song in random_songs:
  print("{}-{}".format(artist,song))
