from config import get_connection_string


def gerar_relatorio_total_consultas_por_clinica():
    try:
        # Conectando ao banco de dados
        conn = get_connection_string()
        cursor = conn.cursor()

        # Consulta SQL para sumarizar o total de consultas por clínica
        query = """
            SELECT C.nome AS clinica_nome, COUNT(Consulta.idConsulta) AS total_consultas
            FROM Clinica C
            LEFT JOIN Consulta ON C.idClinica = Consulta.clinicaId
            GROUP BY C.nome
            ORDER BY total_consultas DESC;
        """

        # Executando a consulta
        cursor.execute(query)

        # Recuperando os resultados
        resultados = cursor.fetchall()

        # Exibindo o relatório
        print(f"{'Clínica':<30}{'Total de Consultas':<20}")
        print("-" * 50)
        for row in resultados:
            print(f"{row[0]:<30}{row[1]:<20}")

    except mysql.connector.Error as err:
        print(f"Erro ao gerar relatório: {err}")
    finally:
        cursor.close()
        conn.close()


def gerar_relatorio_consultas_com_juncao():
    try:
        # Conectando ao banco de dados
        conn = get_connection_string()
        cursor = conn.cursor()

        # Consulta SQL com junção de tabelas
        query = """
            SELECT Consulta.idConsulta, Consulta.dataHora, 
                   Medico.nome AS nome_medico, 
                   Paciente.nome AS nome_paciente, 
                   Clinica.nome AS nome_clinica
            FROM Consulta
            JOIN Medico ON Consulta.medicoId = Medico.idMedico
            JOIN Paciente ON Consulta.pacienteId = Paciente.idPaciente
            JOIN Clinica ON Consulta.clinicaId = Clinica.idClinica
            ORDER BY Consulta.dataHora DESC;
        """

        # Executando a consulta
        cursor.execute(query)

        # Recuperando os resultados
        resultados = cursor.fetchall()

        # Exibindo o relatório
        print(f"{'Consulta ID':<12}{'Data e Hora':<20}{'Médico':<20}{'Paciente':<20}{'Clínica':<30}")
        print("-" * 90)
        for row in resultados:
            print(f"{row[0]:<12}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<30}")

    except mysql.connector.Error as err:
        print(f"Erro ao gerar relatório: {err}")
    finally:
        cursor.close()
        conn.close()