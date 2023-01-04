import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=elei%C3%A7%C3%B5es+presidenciais+brasileiras+2022&rlz=1C1GCEA_enBR995BR995' \
          '&sxsrf=ALiCzsYZ7hgu1H-P5fxTEpxOe-aS6GIOHA%3A1667159818237&ei=CtdeY4WYDvOw5OUPlPaRwAE&oq=Elei%C3%A7%C3%B5es' \
          '+Presidencia&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABB' \
          'CxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCxAxCDATILCAAQgAQQsQMQgwE6BAguEEM6CAguELEDEIMBOgQIIxAnOgoI' \
          'ABCxAxCDARBDOgwIABCxAxCDARAKEEM6BAgAEEM6BQgAEIAESgQIQRgASgQIRhgAUABYsidgqjZoAHAAeACAAbcBiAH6EZIBBDAuMjCYAQ' \
          'CgAQHAAQE&sclient=gws-wiz-serp'

    # MY USER AGENT
chave = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                           (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

site = requests.get(url, headers=chave)
soup = BeautifulSoup(site.content, 'html.parser')

porcentagem = soup.find('div', 'W48ibf').get_text()
print(porcentagem)
