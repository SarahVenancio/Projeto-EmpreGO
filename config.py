ambiente = 'desenvolvimento'

if ambiente == 'desenvolvimento':
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'emprego'

#Chave secreta (session)
SECRET_KEY = 'emprego'

#Acesso adm
MASTER_EMAIL = 'adm@adm'
MASTER_PASSWORD = 'adm'