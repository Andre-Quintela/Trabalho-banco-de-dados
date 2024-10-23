from controllers import clinica, consulta, medico, paciente



def Menu():  
    while True:  
        try:
            resposta = int(input('''
                ===============================================================
                ===== Digite um número referente a opção que você deseja: ===== 
                ===== 1 - Funções para clinicas;                          =====                 
                ===== 2 - Funções para usuários (Médico ou paciente);     =====
                ===== 3 - Marcar nova consulta;                           =====
                ===== 4 - Consultar as consultas marcadas ;               =====
                ===== 5 - Cancelar agendamento de consulta;               =====
                ===== 0 - Sair;                                           =====
                ===============================================================
                '''))
            if resposta not in range(0, 6):
                print("Insira um valor válido.")
            elif resposta == 0:
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
                    medico.cadastrarMedico()
                elif tipo_usuario == 2:
                    paciente.cadastrarPaciente()

            elif resposta == 3:
                print("Consultando usuário...")
                print("1 - Médico")
                print("2 - Paciente")
                tipo_usuario = int(input("Digite o tipo de usuário que deseja consultar: "))
                
                if tipo_usuario == 1:
                    print("1 - Consultar médico por ID")
                    print("2 - Consultar todos os médicos")
                    print("3 - Atualizar médico")
                    print("4 - Deletar médico")
                    resposta = int(input("Digite a opção desejada: "))

                    if resposta == 1:
                        medico.consultarMedicoPorId()
                    elif resposta == 2:
                        medico.consultarMedicos()
                    elif resposta == 3:
                        medico.atualizarMedico()
                    elif resposta == 4:
                        medico.deletarMedico()

                elif tipo_usuario == 2:
                    print("1 - Consultar paciente por ID")
                    print("2 - Consultar todos os pacientes")
                    print("3 - Atualizar paciente")
                    print("4 - Deletar paciente")
                    resposta = int(input("Digite a opção desejada: "))

                    if resposta == 1:
                        paciente.consultarPacientePorId()
                    elif resposta == 2:
                        paciente.consultarPacientes()
                    elif resposta == 3:
                        paciente.atualizarPaciente()
                    elif resposta == 4:
                        paciente.deletarPaciente()

                elif resposta == 3:
                   print("Marcando nova consulta...")
                   consulta.cadastrarConsulta()
                
                elif resposta == 4:
                    print("Consultando consultas marcadas...")
                    print("1 - Consultar consulta por ID")
                    print("2 - Consultar todas as consultas")                    
                    resposta = int(input("Digite a opção desejada: "))
                    
                    if resposta == 1:
                        consulta.consultarConsultaPorId()
                    elif resposta == 2:
                        consulta.consultarConsultas()
                
                elif resposta == 5:
                    print("Cancelando agendamento de consulta...")
                    consulta.deletarConsulta()


           
        except ValueError:
            print("Por favor, insira apenas números.")
