
from database import Database


class Cliente(Database):
    def __init__(self,
                 id=None,
                 nome=None,
                 telefone=None,
                 email=None,
                 password=None):
        super().__init__()
        if id is not None:
            data = self.get(id)
            self.id = data[0]
            self.nome = data[1]
            self.telefone = data[2]
            self.email = data[3]
            self.hash_pass = data[4]
        else:
            self.nome = nome
            self.telefone = telefone
            self.email = email
            self.hash_pass = password
        
    def post(self):
        query = """
        INSERT INTO Cliente (nome, telefone, email, hash_pass)
        VALUES (?, ?, ?, ?);
        """
        return self.execute(query, (
            self.nome,
            self.telefone,
            self.email,
            self.hash_pass
        ))

    def get(self, id):
        query = """
        SELECT * FROM Cliente
        WHERE id_cli = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()
    
    def __repr__(self) -> str:
        return f"{self.id:3}| {self.nome}"

        