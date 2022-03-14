import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from hashlib import md5
import os
from datetime import datetime

a = [] # Cria uma lista com todas as páginas a serem extraídas
for i in range(1,2):
    link = "https://g1.globo.com/politica/index/feed/pagina-{}.ghtml".format(i) 
    a.append(link) 

def web_scrapping_g1():
##########################################################################################################################
# Obter os links de notícias em cada página da lista a, e transformar em BeautifulSoup Object
    start_time = datetime.now()
    with open ('text.txt', 'w', encoding='utf-8') as text_txt:
        for i in a:
            html = requests.get(i)
            bs_g1 = bs(html.content,'lxml')
            for i in bs_g1.find_all('div', {'class': '_evt'}): # Acha a classe _evt, que é onde estão os links de notícias
                links = i.find_all('a', href=True) # Pega somente o link da notícia 
                for link in links:
                    print(link['href'], file=text_txt) 
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))               
##########################################################################################################################
# Retira os itens duplicados, com a biblioteca hashlib
    start_time = datetime.now()
    output_caminho = "text_2.txt" 
    input_caminho = "text.txt"
    completo = set()
    output_arquivo = open(output_caminho, "w") 

    for line in open(input_caminho, "r"):
        hashValue = md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashValue not in completo:
            output_arquivo.write(line)
            completo.add(hashValue)

    output_arquivo.close()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))    
##########################################################################################################################
# Remove os links com "index" , "video" e "ao-vivo" na url, pois não são notícias
    start_time = datetime.now()
    with open("text_2.txt", "r") as input:
        with open("text_out.txt", "w") as output:
            for line in input:                
                if "/index/" not in line.strip("\n"):
                    output.write(line)

    os.replace('text_out.txt', 'text_2.txt')
    
    
    with open("text_2.txt", "r") as input:
        with open("text_out.txt", "w") as output:
            for line in input:                
                if "/ao-vivo/" not in line.strip("\n"):
                    output.write(line)

    os.replace('text_out.txt', 'text_2.txt')

    
    with open("text_2.txt", "r") as input:
        with open("text_out.txt", "w") as output:
            for line in input:                
                if "/video/" not in line.strip("\n"):
                    output.write(line)

    os.replace('text_out.txt', 'text_2.txt')
    
    
    with open("text_2.txt", "r") as input:
        with open("text_out.txt", "w") as output:
            for line in input:                
                if "/playlist/" not in line.strip("\n"):
                    output.write(line)

    os.replace('text_out.txt', 'text_2.txt')
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
#########################################################################################################################
# Adiciona as manchestes de cada notícia em um arquivo
    start_time = datetime.now()
    with open ('text_2_headlines.txt','w', encoding='utf-8') as headlines:
        with open ('text_2.txt','r') as text_2_text:
            for linhas in text_2_text:
                url = urlopen(linhas)
                bs_g1 = bs(url,'lxml')
                manchetes = bs_g1.title.text.split('|')[0].strip().rstrip('\n')    
                print(manchetes, file=headlines)
                
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
                
#########################################################################################################################
# Obter as datas de cada notícia
    start_time = datetime.now()
    with open ('text_2_data.txt','w', encoding='utf-8') as datas:
        with open ('text_2.txt','r') as text_2_text:
            for linhas in text_2_text:
                url = urlopen(linhas)
                bs_g1 = bs(url,'lxml')
                data = bs_g1.find('time')['datetime']
                print(data, file=datas)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))  
