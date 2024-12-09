ambiente = 'desenvolvimento'

if ambiente == 'desenvolvimento':
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'emprego'

if ambiente == 'producao':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'SarahVenancio.mysql.pythonanywhere-services.com'
    DB_USER = 'SarahVenancio'
    DB_PASSWORD = 'meSiv@9184'
    DB_NAME = 'SarahVenancio$blog'

#Chave secreta (session)
SECRET_KEY = 'emprego'

#Acesso adm
MASTER_EMAIL = 'adm@adm'
MASTER_PASSWORD = 'adm'