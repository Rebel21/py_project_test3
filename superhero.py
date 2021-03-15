from pprint import pprint as pp

import requests

URL = 'https://superheroapi.com/api/2619421814940190/'


def get_superhero_intelligence(heroes_list: list):
    heroes_intelligence = {}
    for hero in heroes_list:
        data = requests.get(f'{URL}search/{hero}', timeout=5).json()['results'][0]
        heroes_intelligence[data['name']] = int(data['powerstats']['intelligence'])
    return sorted(heroes_intelligence.items())[-1][0]


pp(get_superhero_intelligence(['Hulk', 'Captain America', 'Thanos']))
