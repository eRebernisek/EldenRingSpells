import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlsxwriter


# Configura o Selenium no ambiente Linux para utilizar o Firefox
firefox = webdriver.Firefox(
    executable_path='./geckodriver')


def openBrowser():
    # Abre o site da Wiki
    firefox.get('https://eldenring.wiki.fextralife.com/Magic+Spells')


def readValues():
    itemList = firefox.find_elements_by_css_selector(
        'a.wiki_link.wiki_tooltip')
    itens = []
    # Formata Valores
    for item in itemList:
        nome = item.text
        itens.append(nome)

    createSheet(itens)


def createSheet(itens):
    livroPlanilha = xlsxwriter.Workbook('Spells.xlsx')
    planilha = livroPlanilha.add_worksheet('Spells')

    rowIndex = 1
    for item in itens:
        planilha.write('A'+str(rowIndex), item)
        rowIndex += 1

    livroPlanilha.close()


if __name__ == '__main__':
    os.system('clear')
    openBrowser()

    time.sleep(10)
    readValues()

    firefox.close()
    quit()
