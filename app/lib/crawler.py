from bs4 import BeautifulSoup, Comment
import requests

BASE_URL = 'https://www.pro-football-reference.com/years/2022/'


def week_urls():
    weeks = []

    for i in range(1, 17):
        weeks.append(f'{BASE_URL}week_{i}.htm')

    return weeks


def game_url_lists():
    game_map = []
    weeks = week_urls()

    for week in weeks:
        games = []
        links = []

        html_text = requests.get(week).text
        soup = BeautifulSoup(html_text, 'lxml')

        summaries = soup.find('div', class_='game_summaries')
        games = summaries.find_all('td', class_='gamelink')

        for game in games:
            a = game.find('a')
            link = week.split('/')
            link.pop()
            link = "/".join(link)
            links.append(link+a['href'])

        game_map.append(links)

    return game_map


print(game_url_lists())
