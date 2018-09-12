# README
# AtozLyric prohibited third-party lyric provider
# This is simply to test html parser
# I want to avoid any issue

import requests
from bs4 import BeautifulSoup

# Creating URL
base = 'https://search.azlyrics.com/search.php?q='
search = list(input('What song do you want to search for? '))
for x in range(len(search)):
    if search[x] == ' ':
        search[x] = '+'

# Full URL
full = base + ''.join(search)

# HMTL parser
r = requests.get(full)
soup = BeautifulSoup(r.text, 'html.parser')
songs = soup.findAll('table')[1].findAll('b')

# Print Songs
for idx, x in enumerate(range(0, len(songs), 2)):
    print('%s: %s -- %s' % (idx + 1, songs[x].text.strip(), songs[x+1].text.strip()))
print(" ")

# Selection of Song
select = int(input('which song it is? ')) - 1
link = soup.findAll('table')[1].findAll('a', href=True)[select]
song_lyric = requests.get(link['href'])

# HTML parser for Lyrics
soup2 = BeautifulSoup(song_lyric.text, 'html.parser')
lyric = soup2.body.findAll('div', class_=None)
for x in lyric:
    print(x.text.strip())
