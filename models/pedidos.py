import mysql.connector
from mysql.connector import Error

DATABASE = 'clinicaDatabase'
USER = 'labdatabase'
PASSWORD = 'lab@Database2022'
HOST = 'localhost'
PORT = '3306'

def consultar_pedidos():
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(
            database = DATABASE,
            user = USER,
            password = PASSWORD,
            host = HOST,
            port = PORT
        )

        if conn.is_connected():
            cursor = conn.cursor()
            print("Conexão bem-sucedida!")

            cursor.execute("SELECT id, cliente_id, data_pedido, valor_total FROM pedidos")
            rows = cursor.fetchall()

            # Exibindo os pedidos
            print("Pedidos:")
            for row in rows:
                print(row)
        else:
            print("Não foi possível conectar ao banco de dados.")
            return

    except Error as err:
        print(f"Erro ao consultar pedidos: {err}")
    
    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()


consultar_pedidos()
