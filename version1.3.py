from requests_html import HTMLSession
from bs4 import BeautifulSoup
from banco import *

session = HTMLSession()
pagina = 1

criar_banco(dia, mes, ano)
conexao_banco()

while True:
    url = (f'https://www.mercadolivre.com.br/ofertas?page={pagina}')
    response = session.get(url)
    html = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:   
        vsql = f'''CREATE TABLE pagina{pagina}(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeProduto VARCHAR(500),
        precoProduto VARCHAR(20),
        pctdescontoProduto VARCHAR(100)
    );'''
        criar_tabela(vcon,vsql,pagina)
    
        if response.url == 'https://www.mercadolivre.com.br/ofertas':
            vcon.close()
            exit()
        else:
            print(f'Página: {pagina}')
                
            for produto in html.select('.promotion-item'):
                titulo = produto.select_one('.promotion-item__title')
                preco = produto.select_one('.promotion-item__price')
                prec = preco.select_one('span')
                cents = produto.select_one('sup',attrs={'.promotion-item__price'})
                off = produto.select_one('span.promotion-item__discount')
                if cents and not off:
                    vsql =  f""" INSERT INTO pagina{pagina}(
                    nomeProduto, precoProduto, pctdescontoProduto
                    )  
                    VALUES( 
                    '"""+titulo.text+"" "' , '""" +f'{prec.text},{cents.text}'+" ""' ,'""" +'null'+"" "');"""
                    inserir(vcon,vsql)
                elif off and not cents:
                    vsql =  f""" INSERT INTO pagina{pagina}(
                    nomeProduto, precoProduto, pctdescontoProduto
                    )  
                    VALUES( 
                    '"""+titulo.text+"" "' , '""" +f'{prec.text}'+" ""' ,'""" +off.text+"" "');""" 
                    inserir(vcon,vsql)     
                elif cents and off:
                    vsql =  f""" INSERT INTO pagina{pagina}(
                    nomeProduto, precoProduto, pctdescontoProduto
                    )  
                    VALUES( 
                    '"""+titulo.text+"" "' , '""" +f'{prec.text},{cents.text}'+" ""' ,'""" +off.text+"" "');"""  
                    inserir(vcon,vsql)
                else:
                    vsql =  f""" INSERT INTO pagina{pagina}(
                    nomeProduto, precoProduto, pctdescontoProduto
                    )  
                    VALUES( 
                    '"""+titulo.text+"" "' , '""" +f'{prec.text}'+" ""' ,'""" +'null'+"" "');"""  
                    inserir(vcon,vsql)
            pagina += 1
            
            
    else:
        vcon.close()
        exit()
        