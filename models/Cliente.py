
from . import Database


class Cliente(Database):
    def __init__(self):
        super().__init__()
        
    def post(self, cli):
        query = """
        INSERT INTO Cliente (nome, email, telefone, hash_pass)
        VALUES (?, ?, ?, ?);
        """
        self.execute(query, cli)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Cliente
        WHERE id_cli = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()
    
    def create_table(self):
        self.execute("""CREATE TABLE  IF NOT EXISTS Cliente (
                                id_cli      INTEGER PRIMARY KEY,
                                nome        TEXT NOT NULL,
                                telefone    TEXT NOT NULL,
                                email       TEXT NOT NULL UNIQUE,
                                hash_pass   TEXT NOT NULL
                        );
                     """)
    

        