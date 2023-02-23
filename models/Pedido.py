from . import Database

class Pedido(Database):
    def __init__(self):
        super().__init__()

    def post(self, ped):
        query = """
        INSERT INTO Pedido (id_cli, id_end, id_ent, data, estado, entrega, total)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        self.execute(query, ped)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Pedido
        WHERE id_ped = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()

    def create_table(self):
        self.execute("""CREATE TABLE IF NOT EXISTS Pedido (
                                id_ped      INTEGER PRIMARY KEY,
                                id_cli      INTEGER NOT NULL REFERENCES Cliente (id_cli),
                                id_end      INTEGER NOT NULL REFERENCES Endereco (id_end),
                                id_ent      INTEGER NOT NULL REFERENCES Entregador (id_ent),
                                data        DATE NOT NULL,
                                estado      TEXT NOT NULL,
                                entrega     REAL NOT NULL,
                                total       REAL NOT NULL
                        );
                     """)
