from config import get_connection_string
from models.clinica_model import Clinica


def cadastrarClinica():
    nome = input("Digite o nome da clínica: ")
    endereco = input("Digite o endereço da clínica: ")
    telefone = input("Digite o telefone da clínica: ")

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    clinica = Clinica(nome=nome, endereco=endereco, telefone=telefone)
    clinica.inserir(conn)
    print(f"Clínica cadastrada com sucesso! ID: {clinica.id_clinica}")

    cursor.close()
    conn.close()

def consultarClinicas():
    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    cursor.execute("SELECT idClinica, nome, endereco, telefone FROM Clinica;")
    clinicas = cursor.fetchall()

    if clinicas:
        print("Clínicas cadastradas:")
        for clinica in clinicas:
            print(f"ID: {clinica[0]}\nNome: {clinica[1]}\nEndereço: {clinica[2]}\nTelefone: {clinica[3]}\n")
    else:
        print("Nenhuma clínica cadastrada.")

    cursor.close()
    conn.close()

def consultarClinicaPorId():
    id_clinica = int(input("Digite o ID da clínica que deseja consultar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    clinica = Clinica.carregar(conn, id_clinica)

    if clinica:
        print(f"Clínica selecionada: {clinica}")
    else:
        print(f"Erro: Clínica com ID {id_clinica} não cadastrada.")

    cursor.close()
    conn.close()

def atualizarClinica():
    id_clinica = int(input("Digite o ID da clínica que deseja atualizar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    clinica = Clinica.carregar(conn, id_clinica)

    if clinica:
        print(f"Clínica selecionada: {clinica}")
        nome = input("Digite o nome da clínica: ")
        endereco = input("Digite o endereço da clínica: ")
        telefone = input("Digite o telefone da clínica: ")

        clinica.nome = nome
        clinica.endereco = endereco
        clinica.telefone = telefone
        clinica.atualizar(conn)
        print("Clínica atualizada com sucesso!")
    else:
        print(f"Erro: Clínica com ID {id_clinica} não cadastrada.")

    cursor.close()
    conn.close()

def deletarClinica():
    id_clinica = int(input("Digite o ID da clínica que deseja deletar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    clinica = Clinica.carregar(conn, id_clinica)

    if clinica:
        print(f"Clínica selecionada: {clinica}")
        confirmacao = input("Tem certeza que deseja deletar esta clínica? (s/N): ")

        if confirmacao.lower() == "s":
            clinica.deletar(conn)
            print("Clínica deletada com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print(f"Erro: Clínica com ID {id_clinica} não cadastrada.")

    cursor.close()
    conn.close()

def numCadastrosClinica():
    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Clinica;")
    num_clinicas = cursor.fetchone()[0]

    print(f"Número de clínicas cadastradas: {num_clinicas}")

    cursor.close()
    conn.close()
    return int(num_clinicas)
