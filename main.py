from bs4 import BeautifulSoup
import pandas as pd
import requests
from requests_html import HTMLSession

url = 'https://www.billboard.com/charts/hot-100'

try:
    session = HTMLSession()
    response = session.get(url)

except requests.exceptions.RequestException as e:
    print(e)

url = 'https://www.billboard.com/charts/hot-100/'

songs = []
artists = []
ranks = []

soup = BeautifulSoup(response.content, "html.parser")


for a in soup.findAll('li', attrs={'class': 'chart-list__element'}):
     song = a.find_next('span', attrs={'class': 'chart-element__information__song'})
     artist = a.find_next('span', attrs={'class': 'chart-element__information__artist'})
     rank = a.find_next('span', attrs={'class': 'chart-element__rank__number'})
     print(rank)
     print(song)
     print(artist)

     songs.append(song)
     artists.append(artist)
     ranks.append(rank)

#print(songs)

df = pd.DataFrame({'Song': songs, 'Artist': artists, 'Rank': rank})

print(df)