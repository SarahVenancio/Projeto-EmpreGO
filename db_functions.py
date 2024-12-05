import mysql.connector
from config import *

#ESTABELECE CONEXÃO COM DB
def conectar_db():
    conexao = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )

    cursor = conexao.cursor(dictionary=True)
    return conexao, cursor

#ENCERRA CONEXÃO COM DB
def encerrar_db(cursor,conexao):
    cursor.close()
    conexao.close()

def limpar_input(campo):
    campolimpo = campo.replace(".","").replace("/","").replace("-","").replace(" ","").replace("(","").replace(")","").replace("R$","")
    return campolimpo