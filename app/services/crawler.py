from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.pro-football-reference.com/years/2022/'

weeks = []

for i in range(1,17):
    weeks.append(f'{BASE_URL}week_{i}.htm')
