from config import get_connection_string
from models.paciente_model import Paciente


def cadastrarPaciente():
    nome = input("Digite o nome do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    data_nascimento = input("Digite a data de nascimento do paciente (formato YYYY-MM-DD): ")
    clinica_id = int(input("Digite o ID da clínica do paciente: "))

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

    # Se a clínica for válida, prossegue com o cadastro do paciente
    paciente = Paciente(nome=nome, endereco=endereco, telefone=telefone, data_nascimento=data_nascimento, clinica_id=clinica_id)
    paciente.inserir(conn)
    print(f"Paciente cadastrado com sucesso! ID: {paciente.id_paciente}")

    cursor.close()
    conn.close()

def consultarPacientePorId():
    id_paciente = int(input("Digite o ID do paciente que deseja consultar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    paciente = Paciente.carregar(conn, id_paciente)

    if paciente:
        print(f"Paciente selecionado: {paciente}")
    else:
        print(f"Erro: Paciente com ID {id_paciente} não cadastrado.")

    cursor.close()
    conn.close()

def consultarPacientes():
    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    cursor.execute("SELECT idPaciente, nome, endereco, telefone, dataNascimento, idClinica FROM Paciente;")
    pacientes = cursor.fetchall()

    if pacientes:
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"ID: {paciente[0]}\nNome: {paciente[1]}\nEndereço: {paciente[2]}\nTelefone: {paciente[3]}\nData de Nascimento: {paciente[4]}\nID da Clínica: {paciente[5]}\n")
    else:
        print("Nenhum paciente cadastrado.")

    cursor.close()
    conn.close()

def atualizarPaciente():
    id_paciente = int(input("Digite o ID do paciente que deseja atualizar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    paciente = Paciente.carregar(conn, id_paciente)

    if paciente:
        print(f"Paciente selecionado: {paciente}")
        nome = input("Digite o nome do paciente: ")
        endereco = input("Digite o endereço do paciente: ")
        telefone = input("Digite o telefone do paciente: ")
        data_nascimento = input("Digite a data de nascimento do paciente (formato YYYY-MM-DD): ")
        clinica_id = int(input("Digite o ID da clínica do paciente: "))

        # Verifica se a clínica existe no banco de dados
        cursor.execute("SELECT idClinica FROM Clinica WHERE idClinica = %s;", (clinica_id,))
        clinica = cursor.fetchone()

        if clinica is None:
            print(f"Erro: A clínica com ID {clinica_id} não está cadastrada.")
            cursor.close()
            conn.close()
            return

        # Se a clínica for válida, prossegue com a atualização do paciente
        paciente.nome = nome
        paciente.endereco = endereco
        paciente.telefone = telefone
        paciente.data_nascimento = data_nascimento
        paciente.clinica_id = clinica_id
        paciente.atualizar(conn)
        print(f"Paciente atualizado com sucesso!")
    else:
        print(f"Erro: Paciente com ID {id_paciente} não cadastrado.")

    cursor.close()
    conn.close()

def deletarPaciente():
    id_paciente = int(input("Digite o ID do paciente que deseja deletar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    paciente = Paciente.carregar(conn, id_paciente)

    if paciente:
        paciente.deletar(conn)
        print(f"Paciente deletado com sucesso!")
    else:
        print(f"Erro: Paciente com ID {id_paciente} não cadastrado.")

    cursor.close()
    conn.close()