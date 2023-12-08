import requests
import json

def getberry(name):
    request = requests.get(f'https://pokeapi.co/api/v2/berry/{name}/')
    response = json.loads(request.content)
    nome = response['firmness']['url']
    print(nome)

if __name__ == '__main__':
    name = input('Insira o id: ')
    getberry(name)

