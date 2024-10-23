from config import get_connection_string
from models import Consulta

def cadastrarConsulta():
    data = input("Digite a data da consulta (formato YYYY-MM-DD): ")
    hora = input("Digite a hora da consulta (formato HH:MM): ")
    medico_id = int(input("Digite o ID do médico da consulta: "))
    paciente_id = int(input("Digite o ID do paciente da consulta: "))
    clinica_id = int(input("Digite o ID da clínica da consulta: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    # Verifica se o médico existe no banco de dados
    cursor.execute("SELECT idMedico FROM Medico WHERE idMedico = %s;", (medico_id,))
    medico = cursor.fetchone()

    if medico is None:
        print(f"Erro: O médico com ID {medico_id} não está cadastrado.")
        cursor.close()
        conn.close()
        return

    # Verifica se o paciente existe no banco de dados
    cursor.execute("SELECT idPaciente FROM Paciente WHERE idPaciente = %s;", (paciente_id,))
    paciente = cursor.fetchone()

    if paciente is None:
        print(f"Erro: O paciente com ID {paciente_id} não está cadastrado.")
        cursor.close()
        conn.close()
        return

    # Verifica se a clínica existe no banco de dados
    cursor.execute("SELECT idClinica FROM Clinica WHERE idClinica = %s;", (clinica_id,))
    clinica = cursor.fetchone()

    if clinica is None:
        print(f"Erro: A clínica com ID {clinica_id} não está cadastrada.")
        cursor.close()
        conn.close()
        return

    # Se o médico, paciente e clínica forem válidos, prossegue com o cadastro da consulta
    consulta = Consulta(data=data, hora=hora, medico_id=medico_id, paciente_id=paciente_id, clinica_id=clinica_id)
    consulta.inserir(conn)
    print(f"Consulta cadastrada com sucesso! ID: {consulta.id_consulta}")

    cursor.close()
    conn.close()

def consultarConsultas():
    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    cursor.execute("SELECT idConsulta, data, hora, medicoId, pacienteId, clinicaId FROM Consulta;")
    consultas = cursor.fetchall()

    if consultas:
        print("Consultas cadastradas:")
        for consulta in consultas:
            print(f"ID: {consulta[0]}\nData: {consulta[1]}\nHora: {consulta[2]}\nID Médico: {consulta[3]}\nID Paciente: {consulta[4]}\nID Clínica: {consulta[5]}\n")
    else:
        print("Nenhuma consulta cadastrada.")

    cursor.close()
    conn.close()

def consultarConsultaPorId():
    id_consulta = int(input("Digite o ID da consulta que deseja consultar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    consulta = Consulta.carregar(conn, id_consulta)

    if consulta:
        print(f"Consulta selecionada: {consulta}")
    else:
        print(f"Erro: Consulta com ID {id_consulta} não cadastrada.")

    cursor.close()
    conn.close()

def atualizarConsulta():
    id_consulta = int(input("Digite o ID da consulta que deseja atualizar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    consulta = Consulta.carregar(conn, id_consulta)

    if consulta:
        print(f"Consulta selecionada: {consulta}")
        data = input("Digite a data da consulta (formato YYYY-MM-DD): ")
        hora = input("Digite a hora da consulta (formato HH:MM): ")
        medico_id = int(input("Digite o ID do médico da consulta: "))
        paciente_id = int(input("Digite o ID do paciente da consulta: "))
        clinica_id = int(input("Digite o ID da clínica da consulta: "))

        # Verifica se o médico existe no banco de dados
        cursor.execute("SELECT idMedico FROM Medico WHERE idMedico = %s;", (medico_id,))
        medico = cursor.fetchone()

        if medico is None:
            print(f"Erro: O médico com ID {medico_id} não está cadastrado.")
            cursor.close()
            conn.close()
            return

        # Verifica se o paciente existe no banco de dados
        cursor.execute("SELECT idPaciente FROM Paciente WHERE idPaciente = %s;", (paciente_id,))
        paciente = cursor.fetchone()

        if paciente is None:
            print(f"Erro: O paciente com ID {paciente_id} não está cadastrado.")
            cursor.close()
            conn.close()
            return

        # Verifica se a clínica existe no banco de dados
        cursor.execute("SELECT idClinica FROM Clinica WHERE idClinica = %s;", (clinica_id,))
        clinica = cursor.fetchone()

        if clinica is None:
            print(f"Erro: A clínica com ID {clinica_id} não está cadastrada.")
            cursor.close()
            conn.close()
            return

        # Se o médico, paciente e clínica forem válidos, prossegue com a atualização da consulta
        consulta.data = data
        consulta.hora = hora
        consulta.medico_id = medico_id
        consulta.paciente_id = paciente_id
        consulta.clinica_id = clinica_id
        consulta.atualizar(conn)
        print("Consulta atualizada com sucesso!")

    else:
        print(f"Erro: Consulta com ID {id_consulta} não cadastrada.")

    cursor.close()
    conn.close()

def deletarConsulta():
    id_consulta = int(input("Digite o ID da consulta que deseja deletar: "))

    conn = get_connection_string()  # Função que retorna a conexão
    cursor = conn.cursor()

    consulta = Consulta.carregar(conn, id_consulta)

    if consulta:
        consulta.deletar(conn)
        print("Consulta deletada com sucesso!")
    else:
        print(f"Erro: Consulta com ID {id_consulta} não cadastrada.")

    cursor.close()
    conn.close()
