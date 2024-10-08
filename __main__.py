import psycopg2
from psycopg2 import sql

# Função para conectar ao PostgreSQL e criar o banco de dados
def create_database():
    try:
        # Conectar ao PostgreSQL (conecte-se ao banco de dados padrão, ex: 'postgres')
        conn = psycopg2.connect(dbname='postgres', user='postgres', password='123', host='localhost', port='5432')
        conn.autocommit = True
        cursor = conn.cursor()

        # Verificar se o banco de dados já existe
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'meu_banco_de_dados'")
        exists = cursor.fetchone()

        if not exists:
            # Criar o banco de dados
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier('meu_banco_de_dados')
            ))
            print("Banco de dados criado com sucesso!")
        else:
            print("Banco de dados já existe.")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")

# Função para criar as tabelas no banco de dados
def create_tables():
    try:
        # Conectar ao banco de dados recém-criado
        conn = psycopg2.connect(dbname='meu_banco_de_dados', user='seu_usuario', password='sua_senha', host='localhost', port='5432')
        conn.set_client_encoding('UTF8')  # Define o encoding para UTF-8
        cursor = conn.cursor()

        # Criação de uma tabela exemplo
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                cpf VARCHAR(14) UNIQUE,
                endereco TEXT,
                telefone VARCHAR(15)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id SERIAL PRIMARY KEY,
                cliente_id INTEGER REFERENCES clientes(id),
                data_pedido DATE,
                valor_total DECIMAL(10, 2)
            );
        """)

        # Confirmar as mudanças
        conn.commit()

        print("Tabelas criadas com sucesso!")
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")

if __name__ == '__main__':
    create_database()
