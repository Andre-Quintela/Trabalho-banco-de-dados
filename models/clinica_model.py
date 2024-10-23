class Clinica:
    def __init__(self, id_clinica=None, nome=None, endereco=None, telefone=None):
        self.id_clinica = id_clinica
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"Clinica(id_clinica={self.id_clinica}, nome='{self.nome}', endereco='{self.endereco}', telefone='{self.telefone}')"

    # Método para simular a inserção de dados
    def inserir(self, conn):
        cursor = conn.cursor()
        query = """
            INSERT INTO Clinica (nome, endereco, telefone)
            VALUES (%s, %s, %s);
        """
        cursor.execute(query, (self.nome, self.endereco, self.telefone))
        self.id_clinica = cursor.lastrowid  # Obtém o ID da última linha inserida
        conn.commit()
        cursor.close()

    # Método para simular a atualização de dados
    def atualizar(self, conn):
        cursor = conn.cursor()
        query = """
            UPDATE Clinica
            SET nome=%s, endereco=%s, telefone=%s
            WHERE idClinica=%s;
        """
        cursor.execute(query, (self.nome, self.endereco, self.telefone, self.id_clinica))
        conn.commit()
        cursor.close()

    # Método para simular a exclusão de dados
    def deletar(self, conn):
        cursor = conn.cursor()
        query = "DELETE FROM Clinica WHERE idClinica=%s;"
        cursor.execute(query, (self.id_clinica,))
        conn.commit()
        cursor.close()
    
    # Método para carregar uma clínica do banco
    @classmethod
    def carregar(cls, conn, id_clinica):
        cursor = conn.cursor()
        query = "SELECT idClinica, nome, endereco, telefone FROM Clinica WHERE idClinica=%s;"
        cursor.execute(query, (id_clinica,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return cls(id_clinica=result[0], nome=result[1], endereco=result[2], telefone=result[3])
        return None
