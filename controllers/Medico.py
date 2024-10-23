from config import get_connection_string
from models import Medico

def cadastrarMedico():
    nome = input("Digite o nome do médico: ")
    especializacao = input("Digite a especialização do médico: ")
    telefone = input("Digite o telefone do médico: ")
    clinica_id = int(input("Digite o ID da clínica do médico: "))
    medico = Medico(nome=nome, especializacao=especializacao, telefone=telefone, clinica_id=clinica_id)
    medico.inserir(**get_connection_string())
    print(f"Médico cadastrado com sucesso! ID: {medico.id_medico}")