from requests_html import HTMLSession
import os
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

session = HTMLSession()
page = 1

def criar_pasta_dia(dia, mes, ano):
            directoryPath = f'/home/davi/Área de Trabalho/Python/bs4 e requests/app1/{dia}_{mes}_{ano}'
            os.mkdir(directoryPath)

criar_pasta_dia(datetime.now().day, datetime.now().month, datetime.now().year)

while page <= 100:
    print(f'Página: {page}')
    url = (f'https://www.mercadolivre.com.br/ofertas?page={page}')
    response = session.get(url)
    html = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:   
        

        def criar_arquivo_ee(dia, mes, ano, page):
            arquivo = Path(f'./app1/{dia}_{mes}_{ano}/ofertas?={dia}_{mes}_{ano}_pt{page}.txt')
            arquivo.touch(exist_ok=True)
            gg = open(arquivo, 'r+')
            for produto in html.select('.promotion-item'):
                titulo = produto.select_one('.promotion-item__title')
                preco = produto.select_one('.promotion-item__price')
                prec = preco.select_one('span')
                cents = produto.select_one('sup',attrs={'.promotion-item__price'})
                off = produto.select_one('span.promotion-item__discount')
                if cents and not off:
                    gg.writelines(f'{titulo.text} | Preço: {prec.text},{cents.text}\n')
                elif off and not cents:
                    gg.writelines(f'{titulo.text} | Preço: {prec.text} | {off.text}\n')         
                elif cents and off:
                    gg.writelines(f'{titulo.text} | Preço: {prec.text},{cents.text} | {off.text}\n')
                else:
                    gg.writelines(f'{titulo.text} | Preço: {prec.text}\n')
        criar_arquivo_ee(datetime.now().day, datetime.now().month, datetime.now().year, page)
    else:
        exit()
    page += 1
        