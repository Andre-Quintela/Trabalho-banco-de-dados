from config import get_connection_string
import mysql.connector
from mysql.connector import Error

def consultar_clientes():
    try:
        conn = mysql.connector.connect(**get_connection_string())
        
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

