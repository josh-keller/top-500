import csv
import random
import wikipedia
from fuzzywuzzy import fuzz
from ytmusicapi import YTMusic

ytmusic = YTMusic()

albums = []

with open('rolling_stone_top_500_albums_2020.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    albums.append(row)

album = random.choice(albums)
artist = album['Artist']
album_name = album['Album']

print("Fetching results for ", album_name, artist)

results = ytmusic.search(query=f"{album_name} {artist}", filter="albums")
wikiInfo = wikipedia.search(f"{album_name} {artist} album")
wikiPage = wikipedia.page(title=wikiInfo[0]).url

browseId = ""
highestRatio = 0

for result in results:
    currRatio = fuzz.ratio(result['title'], album_name)

    if currRatio > highestRatio and result['artists'][0]['name'] == artist:
        browseId = result['browseId']
        highestRatio = currRatio

if browseId:
    album_info = ytmusic.get_album(browseId)
    print("https://music.youtube.com/playlist?list=" + album_info['audioPlaylistId'])
    print(wikiPage)
else:
    print("Could not find link.")
