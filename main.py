from bs4 import BeautifulSoup
import pandas as pd
import requests
from requests_html import HTMLSession
from datetime import date
import datetime

url = 'https://www.billboard.com/charts/hot-100'

origURL = 'https://www.billboard.com/charts/hot-100/'

songs = []
artists = []
ranks = []

today = datetime.datetime.today()
startDateobj = datetime.datetime.strptime('January 30, 2020', '%B %d, %Y')
pageDateobj = startDateobj


# ====================== FUNCTIONS =================
def get_weeks_list():

    for a in soup.findAll('li', attrs={'class': 'chart-list__element'}):
        song = a.find_next('span', attrs={'class': 'chart-element__information__song'})
        artist = a.find_next('span', attrs={'class': 'chart-element__information__artist'})
        rank = a.find_next('span', attrs={'class': 'chart-element__rank__number'})
        #print(rank)
        #print(song)
        #print(artist)
        if int(rank.text) < 10:
            songs.append(song.text)
            artists.append(artist.text)
            ranks.append(int(rank.text))
    return pd.DataFrame({'Song': songs, 'Artist': artists, 'Rank': ranks})


# ================ Not Function WORK ====================

df = pd.DataFrame({'Song': songs, 'Artist': artists, 'Rank': ranks})

while pageDateobj < today:
    url = origURL + str(pageDateobj.date())
    print(url)

    try:
        session = HTMLSession()
        response = session.get(url)

    except requests.exceptions.RequestException as e:
        print(e)

    soup = BeautifulSoup(response.content, "html.parser")

    dateButton = soup.find('button', attrs={'class': 'date-selector__button'})
    pageDate = (str(dateButton.text).strip())
    pageDateobj = datetime.datetime.strptime(pageDate, '%B %d, %Y')
    get_weeks_list()

    frames = [df, get_weeks_list()]
    df = pd.concat(frames)
    pageDateobj = pageDateobj + datetime.timedelta(days=7)

df.sort_values(by='Rank', inplace=True)
df.drop_duplicates(subset='Song', inplace=True)
df.to_csv('music.csv')
