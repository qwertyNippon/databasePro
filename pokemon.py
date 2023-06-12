import requests, json

# name, at least one ability's name, base_experience, 
# and the URL for its sprite (an image that shows up 
# on screen) for the 'front_shiny'

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data1 = res1.json()
    info = data1['name']
    data_dict['name'] = data1['name']
    # data_dict['sprite'] = data1['sprites']['front_shinny']
    print(data_dict)

func('clefairy')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    info = data['name']['abilities'][0]['ability']
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['ability']
    print(data_dict)

func('speed')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    info = data['name']['abilities'][0]['ability']
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['ability']
    print(data_dict)

func('charmander')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    info = data['name']['abilities'][0]['ability']
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['ability']
    print(data_dict)

func('dito')

def func(poke):
    data_dict = {}
    res1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    data = res1.json()
    info = data['name']['abilities'][0]['ability']
    data_dict['name'] = data['name']
    data_dict['abilities'] = data['ability']
    print(data_dict)

func('mew')