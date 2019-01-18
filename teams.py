import requests
import sqlite3
from bs4 import BeautifulSoup

team_url = 'https://www.basketball-reference.com/teams/'

with requests.get(team_url) as r:
    soup = BeautifulSoup(r.text)
    data = soup.find_all(attrs={"data-stat": "franch_name"})


teams = []
for line in data:
    x = str(line.contents).split('>')
    if len(x) is not 1:
        teams.append(x[1].rstrip('</a'))

