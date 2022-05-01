import sqlite3
from sqlite3 import Error
import os
from datetime import datetime

dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year

def criar_banco(dia,mes,ano):
    try:
        os.system(f'touch {dia}_{mes}_{ano}.db')
    except:
        print("Erro! Provavelmente já existe algum arquivo com essa data.")
        exit()



### Conexão ###
def conexao_banco():
    caminho = f'{dia}_{mes}_{ano}.db'
    con = None

    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con

vcon = conexao_banco()

### Criar Tabela ###


def criar_tabela(conexao,sql,pg):
    pg = ''
    try:
        c=conexao.cursor()
        c.execute(sql)
    except Error as er:
        print(er)


#criar_tabela(vcon,vsql,pg)


def inserir(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)


def consultar(conexao,sql):
        c = conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado



'''vsql = 'SELECT * FROM pagina2'
res = consultar(vcon,vsql)

for r in res:
    print(r)'''