from config import get_connection_string
import mysql.connector
from mysql.connector import Error


def consultar_pedidos():
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**get_connection_string())

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
