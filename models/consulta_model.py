class Consulta:
    def __init__(self, id_consulta=None, data_hora=None, medico_id=None, paciente_id=None, clinica_id=None):
        self.id_consulta = id_consulta
        self.data_hora = data_hora  # dataHora na tabela do banco
        self.medico_id = medico_id  # medicoId na tabela do banco
        self.paciente_id = paciente_id  # pacienteId na tabela do banco
        self.clinica_id = clinica_id  # clinicaId na tabela do banco

    def __str__(self):
        return f"Consulta(id_consulta={self.id_consulta}, data_hora={self.data_hora}, medico_id={self.medico_id}, paciente_id={self.paciente_id}, clinica_id={self.clinica_id})"

    # Método para inserir uma nova consulta
    def inserir(self, conn):
        cursor = conn.cursor()
        query = """
            INSERT INTO Consulta (dataHora, medicoId, pacienteId, clinicaId)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (self.data_hora, self.medico_id, self.paciente_id, self.clinica_id))
        self.id_consulta = cursor.lastrowid  # Obtém o ID da última linha inserida
        conn.commit()
        cursor.close()

    # Método para atualizar uma consulta existente
    def atualizar(self, conn):
        cursor = conn.cursor()
        query = """
            UPDATE Consulta
            SET dataHora=%s, medicoId=%s, pacienteId=%s, clinicaId=%s
            WHERE idConsulta=%s;
        """
        cursor.execute(query, (self.data_hora, self.medico_id, self.paciente_id, self.id_consulta, self.clinica_id))
        conn.commit()
        cursor.close()

    # Método para deletar uma consulta
    def deletar(self, conn):
        cursor = conn.cursor()
        query = "DELETE FROM Consulta WHERE idConsulta=%s;"
        cursor.execute(query, (self.id_consulta,))
        conn.commit()
        cursor.close()

    # Método para carregar uma consulta do banco de dados pelo ID
    @classmethod
    def carregar(cls, conn, id_consulta):
        cursor = conn.cursor()
        query = """
            SELECT idConsulta, dataHora, medicoId, pacienteId, clinicaId
            FROM Consulta
            WHERE idConsulta=%s;
        """
        cursor.execute(query, (id_consulta,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return cls(id_consulta=result[0], data_hora=result[1], medico_id=result[2], paciente_id=result[3], clinica_id=result[4])
        return None
