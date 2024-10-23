class Paciente:
    def __init__(self, id_paciente=None, nome=None, endereco=None, telefone=None, data_nascimento=None, clinica_id=None):
        self.id_paciente = id_paciente
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.clinica_id = clinica_id

    def __str__(self):
        return f"Paciente(id_paciente={self.id_paciente}, nome='{self.nome}', endereco='{self.endereco}', telefone='{self.telefone}', data_nascimento={self.data_nascimento}, clinica_id={self.clinica_id})"

    # Método para inserir um novo paciente
    def inserir(self, conn):
        cursor = conn.cursor()
        query = """
            INSERT INTO Paciente (nome, endereco, telefone, dataNascimento, clinicaId)
            VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (self.nome, self.endereco, self.telefone, self.data_nascimento, self.clinica_id))
        self.id_paciente = cursor.lastrowid  # Obtém o ID da última linha inserida
        conn.commit()
        cursor.close()

    # Método para atualizar um paciente existente
    def atualizar(self, conn):
        cursor = conn.cursor()
        query = """
            UPDATE Paciente
            SET nome=%s, endereco=%s, telefone=%s, dataNascimento=%s, clinicaId=%s
            WHERE idPaciente=%s;
        """
        cursor.execute(query, (self.nome, self.endereco, self.telefone, self.data_nascimento, self.clinica_id, self.id_paciente))
        conn.commit()
        cursor.close()

    # Método para deletar um paciente
    def deletar(self, conn):
        cursor = conn.cursor()
        query = "DELETE FROM Paciente WHERE idPaciente=%s;"
        cursor.execute(query, (self.id_paciente,))
        conn.commit()
        cursor.close()

    # Método para carregar um paciente do banco de dados pelo ID
    @classmethod
    def carregar(cls, conn, id_paciente):
        cursor = conn.cursor()
        query = """
            SELECT idPaciente, nome, endereco, telefone, dataNascimento, clinicaId
            FROM Paciente
            WHERE idPaciente=%s;
        """
        cursor.execute(query, (id_paciente,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return cls(id_paciente=result[0], nome=result[1], endereco=result[2], telefone=result[3], data_nascimento=result[4], clinica_id=result[5])
        return None
