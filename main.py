import requests
from bs4 import BeautifulSoup



date = input('Which year you wanna time travel ? temme date in YYYYMMDD:  ')

URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in all_songs]
print(song_names)



# chart-element__information
# chart-element__information__song text--truncate color--primary