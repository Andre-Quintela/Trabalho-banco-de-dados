from Config import get_connection_string
import Config
import mysql.connector
from mysql.connector import errorcode


def create_database():
    try:
        conn = mysql.connector.connect(**get_connection_string())
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{Config.DATABASE}'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(f"CREATE DATABASE {Config.DATABASE}")
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
        conn = mysql.connector.connect(**get_connection_string())
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
                CREATE TABLE IF NOT EXISTS Consulta (
                idConsulta SERIAL PRIMARY KEY,
                dataHora TIMESTAMP NOT NULL,
                status VARCHAR(50),
                medicoId INT REFERENCES Medico(idMedico),
                pacienteId INT REFERENCES Paciente(idPaciente)
            );
        """)

        print("Tabelas criadas com sucesso!")
    except mysql.connector.Error as err:
         print(f"Erro ao criar tabelas: {err}")
    finally:
        cursor.close()
        conn.close()

