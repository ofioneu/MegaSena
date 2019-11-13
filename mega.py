from bs4 import BeautifulSoup
import requests
from datetime import date
import codecs
import psycopg2

try:
    conn = psycopg2.connect(user = "postgres",
                                password = "root",
                                host = "localhost",
                                port = "5432",
                                database = "MegaSena")
    print("BD Conectado!")
    cur = conn.cursor()
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    print("Falha conexao com o banco!")

finally:
    def scraping():

       

       
       vet =[]
       soup = BeautifulSoup(open("d_mega.html"), "html.parser")
       mydivs = soup.find("table")
       dados_html=mydivs.find_all('tr')
       print(len(dados_html))

       #for que passa os ddos html para um vetor
       for i in dados_html:
          vet.append(i.text)   
                
       print(vet[2])
       
       insert_query = "insert into megasena (id, concurso, data_sorteio, primeira_dez, segunda_dez, terceira_dez, quarta_dez, quinta_dez, sexta_dez, arrecadacao_total, ganhadores_sena, cidade, uf, rateio_sena, ganhadores_quina, rateio_quina, ganhadores_quadra, rateio_quadra, acomulado, valor_acomulado, estimativa_premio, acomulado_mega_da_virada) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       dados_insert = (vet[2])

       cur.execute(insert_query, dados_insert)

       recset = cur.fetchall()
       print(recset)

      # tamanho_vet = len(vet)
       #for que le os dados das posições de um vetor
       #for percorre in range(tamanho_vet):
          # for elementos in vet[percorre]:
             #  print(elementos)
            
       


scraping()
