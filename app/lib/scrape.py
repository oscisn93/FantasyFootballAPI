""" beautifuyl qb stat web scraper """
from bs4 import BeautifulSoup, Comment
import json
import requests


def get_player_data(id_: str):
    """ grap quarterback data and format it as json """
    url = 'https://www.pro-football-reference.com/boxscores/202209080ram.htm'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    """
        The data is always in a commented out section 
        so we have to search for a commented out section
        and reparse it as html, as we cant use find() on
        Comment objects.
    """

    table = soup.find('div', attrs={'id': id_}).find(
        text=lambda t: isinstance(t, Comment)
    )

    if table:
        table_rows = BeautifulSoup(table, 'lxml').find_all('tr')
    else:
        table_rows = soup.find('div', attrs={'id': id_}).find_all('tr')

    players = []
    for tr in table_rows:
        names = tr.find_all('th', class_='left')
        for name in names:
            name = name.find('a')
            if not name:
                continue

            qb = {name.text: {}}
            stats = tr.find_all('td', class_='right')
            for stat in stats:
                qb[name.text][stat.attrs['data-stat']] = stat.text

            if 'pass_att' in qb[name.text].keys() and int(qb[name.text]['pass_att']) == 0:
                continue
            if 'punt' in qb[name.text].keys() and int(qb[name.text]['punt']) != 0:
                continue
            team = tr.find('td', class_='left')
            qb[name.text]['team'] = team.text
            players.append(qb)
    return players


def print_json():
    player = []
    player_ids = {
        'pass': 'div_player_offense'
    }
    for type, id_ in player_ids.items():
        player.append({type: get_player_data(id_)})
    print(json.dumps(player))


if __name__ == '__main__':
    print_json()

url_2022_season = 'https://www.pro-football-reference.com/years/2022/'
