from config import get_connection_string
import config
import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        conn = mysql.connector.connect(user=config.USER, password=config.PASSWORD, host=config.HOST, port=config.PORT)
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{config.DATABASE}'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(f"CREATE DATABASE {config.DATABASE}")
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
        conn = get_connection_string()
        conn.autocommit = True 
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clinica (
                idClinica INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                endereco VARCHAR(200),
                telefone VARCHAR(15)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Medico (
                idMedico INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                especializacao VARCHAR(100),
                telefone VARCHAR(15),
                clinicaId INT,
                FOREIGN KEY (clinicaId) REFERENCES Clinica(idClinica)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Paciente (
                idPaciente INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                endereco VARCHAR(200),
                telefone VARCHAR(15),
                dataNascimento DATE,
                clinicaId INT,
                FOREIGN KEY (clinicaId) REFERENCES Clinica(idClinica)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Consulta (
                idConsulta INT AUTO_INCREMENT PRIMARY KEY,
                dataHora TIMESTAMP NOT NULL,
                status VARCHAR(50),
                medicoId INT,
                pacienteId INT,
                clinicaId INT,
                FOREIGN KEY (medicoId) REFERENCES Medico(idMedico),
                FOREIGN KEY (pacienteId) REFERENCES Paciente(idPaciente),
                FOREIGN KEY (clinicaId) REFERENCES Clinica(idClinica)
            );
        """)

        print("Tabelas criadas com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar tabelas: {err}")
    finally:
        cursor.close()
        conn.close()
