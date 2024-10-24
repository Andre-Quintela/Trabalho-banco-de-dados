from controllers import clinica, consulta, medico, paciente
from controllers.relatorios import gerar_relatorio_consultas_com_juncao, gerar_relatorio_total_consultas_por_clinica
from views.splashscreen import splashscreen

def printar():
    for _ in range(100):
        print()

def exibir_menu(opcoes):
    print("\n".join(opcoes))
    return input("Escolha uma opção: ")

def menu_clinica():
    while True:
        resposta = exibir_menu([
            "1 - Cadastrar clínica",
            "2 - Consultar clínicas",
            "3 - Consultar clínica por ID",
            "4 - Atualizar clínica",
            "5 - Deletar clínica",
            "0 - Voltar"
        ])
        if resposta == "1":
            printar()
            clinica.cadastrarClinica()
        elif resposta == "2":
            printar()
            clinica.consultarClinicas()
        elif resposta == "3":
            printar()
            clinica.consultarClinicaPorId()
        elif resposta == "4":
            printar()
            clinica.atualizarClinica()
        elif resposta == "5":
            printar()
            clinica.deletarClinica()
        elif resposta == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuarios():
    while True:
        tipo_usuario = exibir_menu([
            "1 - Médico",
            "2 - Paciente",
            "0 - Voltar"
        ])
        if tipo_usuario == "1":
            printar()
            menu_medico()
        elif tipo_usuario == "2":
            printar()
            menu_paciente()
        elif tipo_usuario == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_medico():
    while True:
        resposta = exibir_menu([
            "1 - Cadastrar médico",
            "2 - Consultar médico por ID",
            "3 - Consultar todos os médicos",
            "4 - Atualizar médico",
            "5 - Deletar médico",
            "0 - Voltar"
        ])
        if resposta == "1":
            printar()
            medico.cadastrarMedico()
        elif resposta == "2":
            printar()
            medico.consultarMedicoPorId()
        elif resposta == "3":
            printar()
            medico.consultarMedicos()
        elif resposta == "4":
            printar()
            medico.atualizarMedico()
        elif resposta == "5":
            printar()
            medico.deletarMedico()
        elif resposta == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_paciente():
    while True:
        resposta = exibir_menu([
            "1 - Cadastrar paciente",
            "2 - Consultar paciente por ID",
            "3 - Consultar todos os pacientes",
            "4 - Atualizar paciente",
            "5 - Deletar paciente",
            "0 - Voltar"
        ])
        if resposta == "1":
            printar()
            paciente.cadastrarPaciente()
        elif resposta == "2":
            printar()
            paciente.consultarPacientePorId()
        elif resposta == "3":
            printar()
            paciente.consultarPacientes()
        elif resposta == "4":
            printar()
            paciente.atualizarPaciente()
        elif resposta == "5":
            printar()
            paciente.deletarPaciente()
        elif resposta == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_consulta():
    while True:
        resposta = exibir_menu([
            "1 - Agendar consulta",
            "2 - Atualizar consulta",
            "3 - Cancelar consulta",
            "4 - Consultar consultas",
            "5 - Consultar consulta por ID",
            "0 - Voltar"
        ])
        if resposta == "1":
            printar()
            consulta.agendarConsulta()
        elif resposta == "2":
            printar()
            consulta.atualizarConsulta()
        elif resposta == "3":
            printar()
            consulta.deletarConsulta()
        elif resposta == "4":
            printar()
            consulta.consultarConsultas()
        elif resposta == "5":
            printar()
            consulta.consultarConsultaPorId()
        elif resposta == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_relatorios():
    while True:
        resposta = exibir_menu([
            "1 - Relatório de consultas por clínica",
            "2 - Relatório de consultas com junção de tabelas",
            "0 - Voltar"
        ])
        if resposta == "1":
            printar()
            gerar_relatorio_total_consultas_por_clinica()
        elif resposta == "2":
            printar()
            gerar_relatorio_consultas_com_juncao()
        elif resposta == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def Menu():
    while True:
        try:
            resposta = exibir_menu([
                "===============================================================",
                "===== Digite um número referente a opção que você deseja: =====",
                "1 - Clinicas",
                "2 - Usuários (Médico ou paciente)",
                "3 - Consulta",
                "4 - Relatórios",
                "0 - Sair",
                "==============================================================="
            ])
            if resposta == "0":
                print("Saindo do programa...")
                break
            elif resposta == "1":
                printar()
                menu_clinica()
            elif resposta == "2":
                printar()
                menu_usuarios()
            elif resposta == "3":
                printar()
                menu_consulta()
            elif resposta == "4":
                printar()
                menu_relatorios()
            else:
                print("Insira um valor válido.")
        except ValueError:
            print("Por favor, insira apenas números.")
