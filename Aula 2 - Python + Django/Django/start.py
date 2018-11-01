import requests

poke1 = requests.get('https://pokeapi.co/api/v2/pokemon/64')
poke1 = requests.get(url)

print(poke1.json()['name'])
