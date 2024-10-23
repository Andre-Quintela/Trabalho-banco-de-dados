from controllers import Medico, Paciente



def Menu():  
    while True:  
        try:
            resposta = int(input('''
                ===============================================================
                ===== Digite um número referente a opção que você deseja: ===== 
                ===== 1 - Cadastrar novo usuário (Médico ou paciente);    =====
                ===== 2 - Consultar os pacientes;                         =====
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
                print("Cadastrando usuário...")
                print("1 - Médico")
                print("2 - Paciente")
                tipo_usuario = int(input("Digite o tipo de usuário que deseja cadastrar: "))

                if tipo_usuario == 1:
                    Medico.cadastrarMedico()
                elif tipo_usuario == 2:
                    Paciente.cadastrarPaciente()
            elif resposta == 2:
                print("Consultando pedidos...")
            elif resposta == 3:
                print("Inserindo um novo valor...")
            elif resposta == 4:
                print("Alterando uma tabela...")
            elif resposta == 5:
                print("Excluindo um valor...")
        except ValueError:
            print("Por favor, insira apenas números.")
