from . import Database


class Entregador(Database):
    def __init__(self):
        super().__init__()

    def post(self, entregador):
        query = """
        INSERT INTO Entregador (nome, placa)
        VALUES (?, ?);
        """
        self.execute(query, entregador)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Entregador
        WHERE id_ent = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()

    def create_table(self):
        self.execute("""CREATE TABLE IF NOT EXISTS Entregador (
                                id_ent      INTEGER PRIMARY KEY,
                                nome        TEXT NOT NULL,
                                placa       TEXT NOT NULL UNIQUE
                        );
                     """)
