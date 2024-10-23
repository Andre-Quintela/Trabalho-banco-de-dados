from time import sleep
from controllers import clinica, consulta, medico, paciente


clinicasCadastradas = clinica.numCadastrosClinica()
medicosCadastrados = medico.numCadastrosMedico()
pacientesCadastrados = paciente.numCadastrosPaciente()
consultasCadastradas = consulta.numCadastrosConsulta()

def splashscreen():
    print(f'''
        ================================================================
                        Sistema de gerenciamento de clínicas        
            TOTAL DE REGISTROS CADASTRADOS:                                     
            1 - Clínicas: {clinicasCadastradas}                  
            2 - Médicos: {medicosCadastrados}                    
            3 - Pacientes: {pacientesCadastrados}                
            4 - Consultas: {consultasCadastradas}                
                                                       
                Criado por: André Quintela                        
                            Cassio Jordan                         
                            Entony Jovino                         
                            Guilherme Ambrozio                   
                            Raphael Simoes                        
                                                          
                Disciplica: Banco de Dados 2024-2                
                 Professor: Howard Roatti                        
        ================================================================
        ''')

    sleep(2)