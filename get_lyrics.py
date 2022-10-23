import bs4
import urllib.request as urllib_request
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.vagalume.com.br/lana-del-rey/'
response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

songs_links = []
songs_names = []
lyrics = []

for item in soup.findAll('a', class_="nameMusic"): 
    link = 'https://www.vagalume.com.br' + item.get('href')
    songs_links.append(link)
    song_name = item.get_text()
    songs_names.append(song_name)
    
for item in songs_links:
    response = urlopen(item)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    lyric = soup.find('div', id='lyrics')
    lyric = " ".join(str(lyric).split()).replace('<br/>', ' ')
    lyric = " ".join(str(lyric).split()).replace(' data-plugin="googleTranslate"', '')
    lyric = " ".join(str(lyric).split()).replace('<div id="lyrics">"', '')
    lyric = " ".join(str(lyric).split()).replace('<div id="lyrics">', '')
    lyric = " ".join(str(lyric).split()).replace('"</div>', '')
    lyrics.append(lyric)
    
lyrics_df = pd.DataFrame()
lyrics_df['Name'] = songs_names
lyrics_df['Link'] = songs_links
lyrics_df['Lyrics'] = lyrics
lyrics_df.to_csv('lyrics.csv')