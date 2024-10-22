from models.clientes import consultar_clientes
from models.pedidos import consultar_pedidos

def Menu():  
    while True:  
        try:
            resposta = int(input('''
                ===============================================================
                ===== Digite um número referente a opção que você deseja: ===== 
                === 1 - Consultar os pedidos;                             =====
                === 2 - Consultar os clientes existentes;                 =====
                === 3 - Inserir um novo valor;                            =====
                === 4 - Alterar uma das tabelas;                          =====
                === 5 - Excluir um valor;                                 =====
                === 0 - Sair;                                             =====
                ===============================================================
                '''))
            if resposta not in range(0, 6):
                print("Insira um valor válido.")
            elif resposta == 0:
                print("Saindo do programa...")
                break
            elif resposta == 1:
                consultar_pedidos()
            elif resposta == 2:
                consultar_clientes()
            elif resposta == 3:
                print("Inserindo um novo valor...")
            elif resposta == 4:
                print("Alterando uma tabela...")
            elif resposta == 5:
                print("Excluindo um valor...")
        except ValueError:
            print("Por favor, insira apenas números.")
