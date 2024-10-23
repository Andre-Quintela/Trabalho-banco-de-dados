class Medico:
    def __init__(self, id_medico=None, nome=None, especializacao=None, telefone=None, clinica_id=None):
        self.id_medico = id_medico
        self.nome = nome
        self.especializacao = especializacao
        self.telefone = telefone
        self.clinica_id = clinica_id

    def __str__(self):
        return f"Medico(id_medico={self.id_medico}, nome='{self.nome}', especializacao='{self.especializacao}', telefone='{self.telefone}', clinica_id={self.clinica_id})"

    # Método para inserir um novo médico
    def inserir(self, conn):
        cursor = conn.cursor()
        query = """
            INSERT INTO Medico (nome, especializacao, telefone, clinicaId)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (self.nome, self.especializacao, self.telefone, self.clinica_id))
        self.id_medico = cursor.lastrowid  # Obtém o ID da última linha inserida
        conn.commit()
        cursor.close()

    # Método para atualizar um médico existente
    def atualizar(self, conn):
        cursor = conn.cursor()
        query = """
            UPDATE Medico
            SET nome=%s, especializacao=%s, telefone=%s, clinicaId=%s
            WHERE idMedico=%s;
        """
        cursor.execute(query, (self.nome, self.especializacao, self.telefone, self.clinica_id, self.id_medico))
        conn.commit()
        cursor.close()

    # Método para deletar um médico
    def deletar(self, conn):
        cursor = conn.cursor()
        query = "DELETE FROM Medico WHERE idMedico=%s;"
        cursor.execute(query, (self.id_medico,))
        conn.commit()
        cursor.close()

    # Método para carregar um médico a partir do banco de dados pelo ID
    @classmethod
    def carregar(cls, conn, id_medico):
        cursor = conn.cursor()
        query = """
            SELECT idMedico, nome, especializacao, telefone, clinicaId
            FROM Medico
            WHERE idMedico=%s;
        """
        cursor.execute(query, (id_medico,))
        result = cursor.fetchone()
        cursor.close()
        
        if result:
            return cls(id_medico=result[0], nome=result[1], especializacao=result[2], telefone=result[3], clinica_id=result[4])
        return None
