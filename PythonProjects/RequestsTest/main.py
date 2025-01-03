import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4b5a7cd1e91de169261d38490c54d686'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_modify = {
    "pokemon_id": "178407",
    "name": "Jonny",
    "photo_id": 2
}

body_inpokeball = {
    "pokemon_id": "178416"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_modify = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_modify)
print(response_modify.text)'''

response_inpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_inpokeball)
print(response_inpokeball.text)