import mysql.connector

def conectar():
    #configuraçoes do banco de dados
    host = 'localhost'
    usuario = 'root'
    senha = 'admin'
    banco_de_dados = 'meubanco'
    
    
    #minha conexão
    conexao = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = banco_de_dados
    )
    
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS aluno(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome varchar(255)
            data_nascimento DATE,
            cidade_natal VARCHAR(255)
            bairro VARCHAR(255)
        )

    ''')
    conexao.commit()
def cadastrar_aluno(conexao,nome,data_nascimento,cidade_natal,bairro):
    cursor = conexao.cursor()
    
    inserir_query = '''
        INSERT INTO aluno (nome,data_nascimento,cidade_natal,bairro)
        VALUES(%s,%s,%s,%s)
    '''
    
    valores = (nome,data_nascimento,cidade_natal,bairro)
    cursor.execute(inserir_query,valores)
    conexao.commit()
        

    




