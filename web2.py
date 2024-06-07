import requests
from bs4 import BeautifulSoup

URL = "https://uzxit.net/turk-mp3"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
audio_turk: list[str] = []
# job_elements = soup.find_all("div", class_="cols fx-row")
data = soup.find_all("div", class_="track-item fx-row fx-middle js-item js-share-item")
for x in data:
    data_track_value = x.get("data-track")
    audio_turk.append(data_track_value)
    print(data_track_value)
