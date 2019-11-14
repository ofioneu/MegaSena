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
       dados_html=mydivs.find_all('tr') #tr retorna um bloco com 21
       print(len(dados_html))

       #for que passa os ddos html para um vetor a cada 21 td corresponde a um resultado
       for i in dados_html:
           if (i != None):
               vet.append(i.text)   
                
       #print(vet[2])
       
       #insert_query = "insert into megasena (id, concurso, data_sorteio, primeira_dez, segunda_dez, terceira_dez, quarta_dez, quinta_dez, sexta_dez, arrecadacao_total, ganhadores_sena, cidade, uf, rateio_sena, ganhadores_quina, rateio_quina, ganhadores_quadra, rateio_quadra, acomulado, valor_acomulado, estimativa_premio, acomulado_mega_da_virada) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       #dados_insert = (vet[2])

       #cur.execute(insert_query, dados_insert)

       #recset = cur.fetchall()
       #print(recset)
       tes=[]
       tes1=[]
       tamanho_vet = len(vet)
       #for que le os dados das posições de um vetor
       #for percorre in range(tamanho_vet):
           #tes1.append(percorre)
           #for elementos in vet[percorre]:
               #for p in range(21):              
                   #tes.append(elementos)
               #del(vet[0:21])
            
       #print(tes) 
       for u in vet[2]:
           tes1.append(u)
       print(vet[2]) 
       print(tes1)

scraping()
