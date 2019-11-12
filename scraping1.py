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

def importa():
   vet_tr =[]
   vet_trtext=[]
   soup = BeautifulSoup(open("d_mega.html"), "html.parser")
   mydivs = soup.find("table")
   h=mydivs.find_all('tr')
   print(len(h))
   for i in h:
       vet_tr.append(i)

   for a in vet_tr[1]:
       vet_trtext.append(a)
   print(vet_trtext)
      
   #f=open('txtmega.txt', 'w')
   #f.writelines(str(vet[1]))
   #f.close()
   #print(vet[1])

importa()

def indiceSemana():
    hoje=date.today()
    indice=hoje.weekday()
    print(indice)
    if(indice==2 or indice==5):
        scraping()

indiceSemana()