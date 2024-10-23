class Consulta:
    def __init__(self, id_consulta=None, data_hora=None, status=None, medico_id=None, paciente_id=None):
        self.id_consulta = id_consulta
        self.data_hora = data_hora
        self.status = status
        self.medico_id = medico_id
        self.paciente_id = paciente_id

    def __str__(self):
        return f"Consulta(id_consulta={self.id_consulta}, data_hora={self.data_hora}, status='{self.status}', medico_id={self.medico_id}, paciente_id={self.paciente_id})"

    # Método para inserir uma nova consulta
    def inserir(self, conn):
        cursor = conn.cursor()
        query = """
            INSERT INTO Consulta (dataHora, status, medicoId, pacienteId)
            VALUES (%s, %s, %s, %s) RETURNING idConsulta;
        """
        cursor.execute(query, (self.data_hora, self.status, self.medico_id, self.paciente_id))
        self.id_consulta = cursor.fetchone()[0]
        conn.commit()
        cursor.close()

    # Método para atualizar uma consulta existente
    def atualizar(self, conn):
        cursor = conn.cursor()
        query = """
            UPDATE Consulta
            SET dataHora=%s, status=%s, medicoId=%s, pacienteId=%s
            WHERE idConsulta=%s;
        """
        cursor.execute(query, (self.data_hora, self.status, self.medico_id, self.paciente_id, self.id_consulta))
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
            SELECT idConsulta, dataHora, status, medicoId, pacienteId
            FROM Consulta
            WHERE idConsulta=%s;
        """
        cursor.execute(query, (id_consulta,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return cls(id_consulta=result[0], data_hora=result[1], status=result[2], medico_id=result[3], paciente_id=result[4])
        return None
