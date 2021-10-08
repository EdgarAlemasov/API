import requests
from pprint import pprint


TOKEN = '2619421814940190'
name = ['Hulk', 'Captain America', 'Thanos']
hero_dict = {}

for hero in name:
  url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
  response = requests.get(url=url, timeout=5)
  result = response.json()

  # pprint(result['results'])

  for info in result['results']:
    # print(info['id'], info['name'], info['powerstats']['intelligence'])
    x = {info['name']:{'id': info['id'], 'intelligence': info['powerstats']['intelligence']}}
    hero_dict.update(x)

# pprint(hero_dict)
the_cleverest_hero = max(hero_dict)


print(f"Самый умный супергерой {the_cleverest_hero} его Intelligence {hero_dict[the_cleverest_hero]['intelligence']}")