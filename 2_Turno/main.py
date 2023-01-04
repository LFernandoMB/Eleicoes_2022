import requests
from bs4 import BeautifulSoup
from PyQt5 import uic, QtWidgets, Qt
from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
from time import sleep

app = QtWidgets.QApplication([])
tela = uic.loadUi("eleicoes.ui")


def loop_principal():
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

    filtro = list()
    base = str(soup.find_all('span', 'GwBOec kKVYgd')).split(">")

    for indice, item in enumerate(base):
        if indice % 2 == 0:
            pass
        else:
            filtro.append(item.replace('</span', ''))

    bozo_perc = filtro[2]
    bozo_votos = filtro[3]

    lula_perc = filtro[0]
    lula_votos = filtro[1]

    brancos_nulos = filtro[5]

    tela.votos_candidato1.setText(lula_votos)
    teste = tela.votos_candidato1.text()
    tela.porcentagem_candidato1.setText(lula_perc)

    tela.votos_candidato2.setText(bozo_votos)
    tela.porcentagem_candidato2.setText(bozo_perc)

    tela.nulos.setText(brancos_nulos)
    tela.total_votos.setText(porcentagem)


# tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
# tela.setWindowOpacity(1)
tela.btnAtualizar.clicked.connect(loop_principal)

tela.show()
app.exec()
