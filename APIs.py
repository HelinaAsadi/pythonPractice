import requests # to be able to send requests

baseUrl = "https://pokeapi.co/api/v2/"

def get_pokemon(name) :
    url = f"{baseUrl}/pokemon/{name}"
    response = requests.get(url)
     # print(response)  # this will return the http header status code
    if response.status_code == 200 :
        pokemon = response.json() # .jason method turns the retrieved object to a python dictionary
        return pokemon
    else :
        print(f"failed to recieve data, status code: {response.status_code}")



pokemon_name = input("Enter a pokemon name: ")
pokemon = get_pokemon(pokemon_name) # it is a dictionary

if pokemon:
    print(f"name : {pokemon["name"]}")
    print(f"id : {pokemon["id"]}")
    print(f"height : {pokemon["height"]}")