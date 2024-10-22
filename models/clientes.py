import mysql.connector
from mysql.connector import Error

DATABASE = 'clinicaDatabase'
USER = 'labdatabase'
PASSWORD = 'lab@Database2022'
HOST = 'localhost'
PORT = '3306'


def consultar_clientes():
    try:
        conn = mysql.connector.connect(
            database = DATABASE,
            user = USER,
            password = PASSWORD,
            host = HOST,
            port = PORT 
        )
        
        if conn.is_connected():
            print("Conexão bem-sucedida!")

            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, cpf, endereco, telefone FROM clientes")
            rows = cursor.fetchall()
            
            # Exibindo os clientes
            print("Clientes:")
            for row in rows:
                print(row)
        else:
            print("Falha na conexão com o banco de dados.")

    except Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
    
    finally:
        # Fechando o cursor e a conexão, se existirem
        if cursor:
            cursor.close()
        if conn:
            conn.close()

