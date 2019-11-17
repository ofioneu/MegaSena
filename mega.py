from bs4 import BeautifulSoup
import requests
from datetime import date,time, datetime
import time
import psycopg2

try:
    conn = psycopg2.connect(user = "postgres",
                                password = "root",
                                host = "localhost",
                                port = "5433",
                                database = "postgres")
    print("BD Conectado!")
    cur = conn.cursor()
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    print("Falha conexao com o banco!")

finally:

        def scrapingInsert():
                page = requests.get('https://www.sorteonline.com.br/mega-sena/resultados/')
                print(page)
                soup = BeautifulSoup(page.text, "html.parser")

                dezenas = soup.find("div", {"class": "result result-default center"})
                filhos_dezenas=dezenas.findChildren("li")

                vet_dezenas =[]

                for filhos in filhos_dezenas:
                        vet_dezenas.append(filhos.text)

                print('Ultimas dezenas: ', vet_dezenas)

                n_concurso = soup.find("span", {"id": "nroConcursoHeader[0]"}).text
                print('Concurso atual: ', n_concurso)

                resultados = soup.find_all("div", {"class": "tr"})
                ganhadoderes_td=[]
                del(resultados[0])
                print('quantidade de classes tr: ',len(resultados))
                for filhos_resultados in resultados:
                        if(filhos_resultados.get_text):
                                ganhadoderes_td.append(filhos_resultados.findChildren("span", {"class":"td"}))

                vet_class_td=[]
                rateio=[]
                rat_sena=[]
                rat_quina=[]
                rat_quadra=[]
                _acomulado=''
                _seq_id_id = 0
                for class_td in ganhadoderes_td:                        
                        vet_class_td.append(class_td)
                for u in range(len(vet_class_td)):                
                        for i in vet_class_td[u]:
                               rateio.append(i.text)
             
                
                for _rat_sena in rateio[:3]:
                        rat_sena.append(_rat_sena.strip().replace('-', '0').replace('.','').replace(',','.'))
                
                for _rat_quina in rateio[3:6]:
                        rat_quina.append(_rat_quina.strip().replace('-', '0').replace('.','').replace(',','.'))
                
                for _rat_quadra in rateio[6:9]:
                        rat_quadra.append(_rat_quadra.strip().replace('-', '0').replace('.','').replace(',','.'))


                if(rat_sena[1]!='0'):
                        _acomulado='NAO'
                else:
                        _acomulado='SIM'

                hj = date.today()
  
                insert_query = "insert into megasena (id, concurso, data_sorteio, primeira_dez,segunda_dez, terceira_dez, quarta_dez, quinta_dez, sexta_dez, ganhadores_sena, rateio_sena, ganhadores_quina, rateio_quina, ganhadores_quadra, rateio_quadra, acomulado) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

                cur.execute('SELECT max(id) as maximo FROM megasena')
                seq_id=cur.fetchone()
                
                for _seq_id in seq_id:                        
                        _seq_id_id=_seq_id
                        print('_seq_id_id for: ', _seq_id_id)
               
                _seq_id_id =int(_seq_id_id) + 1 
                print('seq_id: ', _seq_id_id)

                values_=(_seq_id_id, n_concurso, hj, vet_dezenas[0],vet_dezenas[1],vet_dezenas[2],vet_dezenas[3],vet_dezenas[4],vet_dezenas[5], rat_sena[1],rat_sena[2], rat_quina[1],rat_quina[2], rat_quadra[1],rat_quadra[2],_acomulado)

                _seq_id_id = 0
                print('Seq_id_id: ', _seq_id_id)
                             
                cur.execute(insert_query,values_)
                              
                conn.commit()
                
                time.sleep(2)
        
        
        
        def controle():
                hoje=date.today()
                hora= datetime.now()
                print('Hora atual: ', hora.hour, hora.minute, hora.second)
                indice=hoje.weekday()
                print('Indice do dia da semana: ', indice)
                if((indice==2 or indice==5) and hora.hour == 22 and hora.minute == 00 and (hora.second == 00 or hora.second == 1)):
                        scrapingInsert()

        
        while True:
                controle()
                time.sleep(1)