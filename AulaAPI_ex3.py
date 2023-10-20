import requests

print ('Github users')

username = input('usuario: ')
#requisição com id (username)
url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(data)
    print('=====================')
    print(f'Nome completo {data["name"]}')
    print(f'bio {data["bio"]}')
    print(f'localização {data["location"]}')
    print(f'seguidores {data["followers"]}')
    print(f'seguindo {data["following"]}') 
else:
    print('Usuário não encontrado!')