from bs4 import BeautifulSoup
import requests
from datetime import date

def scraping():
    page = requests.get('https://www.sorteonline.com.br/mega-sena/resultados/')
    print(page)
    soup = BeautifulSoup(page.text, "html.parser")

    mydivs = soup.find("div", {"class": "result result-default center"})
    filhos=mydivs.findChildren("li")

    vet_filhos =[]

    for child in filhos:
        vet_filhos.append(child.text)

    print(vet_filhos)

def indiceSemana():
    hoje=date.today()
    indice=hoje.weekday()
    print(indice)
    if(indice==2 or indice==5):
        scraping()

indiceSemana()