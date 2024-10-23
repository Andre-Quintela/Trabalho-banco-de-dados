from config import get_connection_string
from models.medico_model import Medico

def cadastrarMedico():
    nome = input("Digite o nome do médico: ")
    especializacao = input("Digite a especialização do médico: ")
    telefone = input("Digite o telefone do médico: ")
    clinica_id = int(input("Digite o ID da clínica do médico: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    # Verifica se a clínica existe no banco de dados
    cursor.execute("SELECT idClinica FROM Clinica WHERE idClinica = %s;", (clinica_id,))
    clinica = cursor.fetchone()

    if clinica is None:
        print(f"Erro: A clínica com ID {clinica_id} não está cadastrada.")
        cursor.close()
        conn.close()
        return

    # Se a clínica for válida, prossegue com o cadastro do médico
    medico = Medico(nome=nome, especializacao=especializacao, telefone=telefone, clinica_id=clinica_id)
    medico.inserir(conn)
    print(f"Médico cadastrado com sucesso! ID: {medico.id_medico}")

    cursor.close()
    conn.close()

def consultarMedicoPorId():
    id_medico = int(input("Digite o ID do médico que deseja consultar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    medico = Medico.carregar(conn, id_medico)

    if medico:
        print(f"Médico selecionado: {medico}")
    else:
        print(f"Erro: Médico com ID {id_medico} não cadastrado.")

    cursor.close()
    conn.close()

def consultarMedicos():
    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    cursor.execute("SELECT idMedico, nome, especializacao, telefone, clinicaId FROM Medico;")
    medicos = cursor.fetchall()

    if medicos:
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"ID: {medico[0]}\nNome: {medico[1]}\nEspecialização: {medico[2]}\nTelefone: {medico[3]}\nClínica ID: {medico[4]}\n")
    else:
        print("Nenhum médico cadastrado.")

    cursor.close()
    conn.close()

def atualizarMedico():
    id_medico = int(input("Digite o ID do médico que deseja atualizar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    medico = Medico.carregar(conn, id_medico)

    if medico:
        print(f"Médico selecionado: {medico}")
        nome = input("Digite o nome do médico: ")
        especializacao = input("Digite a especialização do médico: ")
        telefone = input("Digite o telefone do médico: ")
        clinica_id = int(input("Digite o ID da clínica do médico: "))

        # Verifica se a clínica existe no banco de dados
        cursor.execute("SELECT idClinica FROM Clinica WHERE idClinica = %s;", (clinica_id,))
        clinica = cursor.fetchone()

        if clinica is None:
            print(f"Erro: A clínica com ID {clinica_id} não está cadastrada.")
            cursor.close()
            conn.close()
            return

        # Se a clínica for válida, prossegue com a atualização do médico
        medico.nome = nome
        medico.especializacao = especializacao
        medico.telefone = telefone
        medico.clinica_id = clinica_id
        medico.atualizar(conn)
        print(f"Médico atualizado com sucesso!")

    else:
        print(f"Erro: Médico com ID {id_medico} não cadastrado.")

    cursor.close()
    conn.close()

def deletarMedico():
    id_medico = int(input("Digite o ID do médico que deseja deletar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    medico = Medico.carregar(conn, id_medico)

    if medico:
        print(f"Médico selecionado: {medico}")
        medico.deletar(conn)
        print("Médico deletado com sucesso!")
    else:
        print(f"Erro: Médico com ID {id_medico} não cadastrado.")

    cursor.close()
    conn.close

def numCadastrosMedico():
    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Medico;")
    num_medicos = cursor.fetchone()[0]
    print(f"Total de médicos cadastrados: {num_medicos}")

    cursor.close()
    conn.close()
    return int(num_medicos)