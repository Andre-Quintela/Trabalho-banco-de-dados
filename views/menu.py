from controllers import clinica, consulta, medico, paciente
from controllers.relatorios import gerar_relatorio_consultas_com_juncao, gerar_relatorio_total_consultas_por_clinica
from views.splashscreen import splashscreen

def Menu():  
    while True:  
        try:
            resposta = int(input('''
                ===============================================================
                ===== Digite um número referente a opção que você deseja: ===== 
                ===== 1 - Clinicas;                                       =====                 
                ===== 2 - Usuários (Médico ou paciente);                  =====
                ===== 3 - Consulta;                                       =====
                ===== 4 - Relatórios                                      =====
                ===== 0 - Sair;                                           =====
                ===============================================================
                '''))
            if resposta not in range(0, 6):
                print("Insira um valor válido.")
            elif resposta == 0:
                splashscreen()
                print("Saindo do programa...")
                break

            elif resposta == 1:
                print("1 - Cadastrar clínica")
                print("2 - Consultar clínicas")
                print("3 - Consultar clínica por ID")
                print("4 - Atualizar clínica")
                print("5 - Deletar clínica")

                resposta = int(input("Digite a opção desejada: "))
                if resposta == 1:
                    clinica.cadastrarClinica()
                elif resposta == 2:
                    clinica.consultarClinicas()
                elif resposta == 3:
                    clinica.consultarClinicaPorId()
                elif resposta == 4:
                    clinica.atualizarClinica()
                elif resposta == 5:
                    clinica.deletarClinica()
                
            elif resposta == 2:
                print("Cadastrando usuário...")
                print("1 - Médico")
                print("2 - Paciente")
                tipo_usuario = int(input("Digite o tipo de usuário que deseja cadastrar: "))
                if tipo_usuario == 1:
                    print("1 - Cadastrar médico")
                    print("2 - Consultar médico por ID")
                    print("3 - Consultar todos os médicos")
                    print("4 - Atualizar médico")
                    print("5 - Deletar médico")
                    resposta = int(input("Digite a opção desejada: "))

                    if resposta == 1:
                        medico.cadastrarMedico()
                    elif resposta == 2:
                        medico.consultarMedicoPorId()        
                    elif resposta == 3:
                        medico.consultarMedicos()
                    elif resposta == 4:
                        medico.atualizarMedico()
                    elif resposta == 5:
                        medico.deletarMedico()

                elif tipo_usuario == 2:
                    print("1 - Cadastrar paciente")
                    print("2 - Consultar paciente por ID")
                    print("3 - Consultar todos os pacientes")
                    print("4 - Atualizar paciente")
                    print("5 - Deletar paciente")
                    resposta = int(input("Digite a opção desejada: "))

                    if resposta == 1:
                        paciente.cadastrarPaciente()
                    elif resposta == 2:
                        paciente.consultarPacientePorId()
                    elif resposta == 3:
                        paciente.consultarPacientes()
                    elif resposta == 4:
                        paciente.atualizarPaciente()
                    elif resposta == 5:
                        paciente.deletarPaciente()

            elif resposta == 3:
                print("1 - Agendar consulta")
                print("2 - Atualizar consulta")
                print("3 - Cancelar consulta")
                print("4 - Consultar consultas")
                print("5 - Consultar consulta por ID")

                resposta = int(input("Digite a opção desejada: "))
                if resposta == 1:
                    consulta.cadastrarConsulta()
                elif resposta == 2:
                    consulta.atualizarConsulta()
                elif resposta == 3:
                    consulta.deletarConsulta()
                elif resposta == 4:
                    consulta.consultarConsultas()
                elif resposta == 5:
                    consulta.consultarConsultaPorId()                  
    
            elif resposta == 4:
                print("1 - Relatório de consultas por clínica")
                print("2 - Relatório de consultas com junção de tabelas")
                resposta = int(input("Digite a opção desejada: "))
                if resposta == 1:
                    gerar_relatorio_total_consultas_por_clinica()
                elif resposta == 2:
                    gerar_relatorio_consultas_com_juncao()
           
        except ValueError:
            print("Por favor, insira apenas números.")
