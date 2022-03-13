def web_scrapping_g1():
    import requests
    from bs4 import BeautifulSoup as bs
    import re
    from urllib.request import urlopen
    import hashlib
    import os
##########################################################################################################################    
# Cria uma lista com todas as páginas a serem extraídas
a = []
for i in range(1,10):
    link = "https://g1.globo.com/politica/index/feed/pagina-{}.ghtml".format(i) 
    a.append(link) 
##########################################################################################################################
# Obter os links de notícias em cada página da lista a, e transformar em BeautifulSoup Object
with open ('text.txt', 'w') as text_txt:
    for i in a:
        html = requests.get(i)
        bs_g1 = bs(html.content)
        for i in bs_g1.find_all('div', {'class': '_evt'}): # Acha a classe _evt, que é onde estão os links de notícias
            links = i.find_all('a', href=True) # Pega somente o link da notícia 
            for link in links:
                print(link['href'], file=text_txt)
                
text_txt.close()               
##########################################################################################################################
# Retira os itens duplicados, com a biblioteca hashlib
output_caminho = "text_2.txt" 
input_caminho = "text.txt"
completo = set()
output_arquivo = open(output_caminho, "w") 

for line in open(input_caminho, "r"):
    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
    if hashValue not in completo:
        output_arquivo.write(line)
        completo.add(hashValue)
        
output_arquivo.close()
##########################################################################################################################
# Remove os links com "index" e "ao-vivo" na url, pois não são notícias
with open("text_2.txt", "r") as input:
    with open("text_out.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if "/index/" not in line.strip("\n"):
                output.write(line)
                
os.replace('text_out.txt', 'text_2.txt')

output.close()
##########################################################################################################################
# # Obter as datas de cada notícia
# with open ('text_2_data.txt','w') as datas:
#     with open ('text_2.txt','r') as text_2_text:
#         for linhas in text_2_text:
#             url = urlopen(linhas)
#             bs_g1 = bs(url)
#             data = bs_g1.find('p', {'class': 'content-publication-data__updated'}).text.rstrip().lstrip()[:-22].strip().replace('h',':')
#             data = data + ':00'
#             print(data, file=datas) #[:-22].strip() deixa só a data e o horário