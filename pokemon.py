import requests, json

# name, at least one ability's name, base_experience, 
# and the URL for its sprite (an image that shows up 
# on screen) for the 'front_shiny'

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['abilities'][0]['ability']
    data_dict['base_experience'] = data['base_experience']
    data_dict['attack'] = data['stats'][0]
    data_dict['attack'] = data['stats'][1]
    data_dict['defense'] = data['stats'][2]
    data_dict['special-attack'] = data['stats'][3]
    data_dict['sprites'] = data['sprites']['front_shiny']
    print(data_dict)

func('gyarados')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['abilities'][0]['ability']
    data_dict['base_experience'] = data['base_experience']
    data_dict['attack'] = data['stats'][0]
    data_dict['attack'] = data['stats'][1]
    data_dict['defense'] = data['stats'][2]
    data_dict['special-attack'] = data['stats'][3]
    data_dict['sprites'] = data['sprites']['front_shiny']
    print(data_dict)

func('zapdos')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['abilities'][0]['ability']
    data_dict['base_experience'] = data['base_experience']
    data_dict['attack'] = data['stats'][0]
    data_dict['attack'] = data['stats'][1]
    data_dict['defense'] = data['stats'][2]
    data_dict['special-attack'] = data['stats'][3]
    data_dict['sprites'] = data['sprites']['front_shiny']
    print(data_dict)

func('lugia')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['abilities'][0]['ability']
    data_dict['base_experience'] = data['base_experience']
    data_dict['attack'] = data['stats'][0]
    data_dict['attack'] = data['stats'][1]
    data_dict['defense'] = data['stats'][2]
    data_dict['special-attack'] = data['stats'][3]
    data_dict['sprites'] = data['sprites']['front_shiny']
    print(data_dict)

func('ditto')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['abilities'][0]['ability']
    data_dict['base_experience'] = data['base_experience']
    data_dict['attack'] = data['stats'][0]
    data_dict['attack'] = data['stats'][1]
    data_dict['defense'] = data['stats'][2]
    data_dict['special-attack'] = data['stats'][3]
    data_dict['sprites'] = data['sprites']['front_shiny']
    print(data_dict)

func('mew')

# pokemon properties to include:
#                 pokemon name
#        from the stats section:
#                  base stat for hp
#                  base stat for defense
#                  base stat for attack
#        from the sprites section:
#                  front_shiny (URL to the image) 
#                  or any other image you like more 
#        from the abilities section:
#                  At Least One Ability
# and any other properties you might find that 
# interest you.