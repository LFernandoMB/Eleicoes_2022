import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import copy

url = 'https://www.google.com/search?q=apura%C3%A7%C3%A3o+elei%C3%A7%C3%B5es+2022&rlz=1C1GCEA_\
enBR995BR995&oq=apura%C3%A7%C3%A3o+&aqs=chrome.2.69i57j0i131i433i512l2j0i131i433l4j69i61.\
3656j0j7&sourceid=chrome&ie=UTF-8'

# MY USER AGENT
chave = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                       (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

site = requests.get(url, headers=chave)
soup = BeautifulSoup(site.content, 'html.parser')

porcentagem = soup.find('div', id='OCxEfd').get_text()

perc_votos = soup.find_all('span', 'GwBOec kKVYgd')

candidatos = soup.find_all('div', 'xKiWDb kKVYgd')

lista_percentual = []
lista_votos = []
lista_candidatos = []

for i, item in enumerate(perc_votos):
    # posi = str(item).find('>')
    if i % 2 == 0:
        lista_percentual.append(str(item)[28:-7])
    else:
        lista_votos.append(str(item)[28:-7])

for i, item in enumerate(candidatos):
    tratar = str(item)[34:]
    posi = tratar.find('"')
    lista_candidatos.append(tratar[:posi])

resultado = zip(lista_candidatos, lista_votos, lista_percentual)
resultado2 = copy.deepcopy(resultado)

df = pd.DataFrame(list(resultado2))
df.to_csv('my_file.csv', encoding='utf-8', sep=';')

print()
print('** ELEIÇÕES 2022 **')
print(f'{porcentagem}\n')
sleep(1)

for teste in resultado:
    print(f'{teste[0]}\n\tVotos: {teste[1]}\n\tPorcentagem: {teste[2]}\n')
    sleep(0.7)
