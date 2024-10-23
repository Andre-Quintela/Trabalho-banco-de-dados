from Config import get_connection_string
from models import Paciente


def cadastrarPaciente():
    nome = input("Digite o nome do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    data_nascimento = input("Digite a data de nascimento do paciente: ")
    clinica_id = int(input("Digite o ID da clínica do paciente: "))
    paciente = Paciente(nome=nome, endereco=endereco, telefone=telefone, data_nascimento=data_nascimento, clinica_id=clinica_id)
    paciente.inserir(**get_connection_string())
    print(f"Paciente cadastrado com sucesso! ID: {paciente.id_paciente}")