import mysql.connector
from mysql.connector import errorcode

DATABASE = 'clinicaDatabase'
USER = 'labdatabase'
PASSWORD = 'lab@Database2022'
HOST = 'localhost'
PORT = '3306'

def create_database():
    try:
        conn = mysql.connector.connect(user = USER, password = PASSWORD, host = HOST, port = PORT)
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{DATABASE}'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(f"CREATE DATABASE {DATABASE}")
            print("Banco de dados criado com sucesso!")
        else:
            print("Banco de dados já existe.")

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
    finally:
        cursor.close()
        conn.close()

def create_tables():
    try:
        conn = mysql.connector.connect(
            database = DATABASE,
            user = USER,
            password = PASSWORD,
            host = HOST,
            port= PORT
        )
        conn.autocommit = True 
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clinica (
                idClinica SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                endereco VARCHAR(200),
                telefone VARCHAR(15)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Medico (
                idMedico SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                especializacao VARCHAR(100),
                telefone VARCHAR(15),
                clinicaId INT REFERENCES Clinica(idClinica)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Paciente (
                idPaciente SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                endereco VARCHAR(200),
                telefone VARCHAR(15),
                dataNascimento DATE,
                clinicaId INT REFERENCES Clinica(idClinica)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Recepcionista (
                idRecepcionista SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                telefone VARCHAR(15),
                clinicaId INT REFERENCES Clinica(idClinica)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Administrador (
                idAdministrador SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                clinicaId INT REFERENCES Clinica(idClinica)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Consulta (
                idConsulta SERIAL PRIMARY KEY,
                dataHora TIMESTAMP NOT NULL,
                status VARCHAR(50),
                medicoId INT REFERENCES Medico(idMedico),
                pacienteId INT REFERENCES Paciente(idPaciente)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Receita (
                idReceita SERIAL PRIMARY KEY,
                nomeMedicamento VARCHAR(100) NOT NULL,
                dosagem VARCHAR(50),
                duracaoDias INT,
                consultaId INT REFERENCES Consulta(idConsulta)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Prontuario (
                idProntuario SERIAL PRIMARY KEY,
                data TIMESTAMP NOT NULL,
                diagnostico VARCHAR(255),
                tratamento VARCHAR(255),
                consultaId INT REFERENCES Consulta(idConsulta)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Faturamento (
                idFaturamento SERIAL PRIMARY KEY,
                valor DECIMAL(10, 2),
                dataFaturamento TIMESTAMP NOT NULL,
                consultaId INT REFERENCES Consulta(idConsulta)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Relatorio (
                idRelatorio SERIAL PRIMARY KEY,
                dataGeracao TIMESTAMP NOT NULL,
                detalhes VARCHAR(255),
                administradorId INT REFERENCES Administrador(idAdministrador)
            );
        """)

        print("Tabelas criadas com sucesso!")
    except mysql.connector.Error as err:
         print(f"Erro ao criar tabelas: {err}")
    finally:
        cursor.close()
        conn.close()
if __name__ == '__main__':
     create_database()
     create_tables()
