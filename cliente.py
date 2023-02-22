import sqlite3

class Cliente(object):
    def __init__(self, nome, telefone, email, password):
        self.id = None
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.hash_pass = password

    def post(self, cursor):
        query = """
        INSERT INTO Cliente (nome, telefone, email, hash_pass)
        VALUES (?, ?, ?, ?);
        """
        return cursor.execute(query, (
            self.nome,
            self.telefone,
            self.email,
            self.hash_pass
        ))

    def get(self, cursor, id):
        query = """
        SELECT * FROM Cliente
        WHERE id = ?
        """
        return cursor.execute(query, id)

    def __repr__(self) -> str:
        return f"{self.id:3}| {self.nome}"
