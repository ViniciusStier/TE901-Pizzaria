from . import Database

class RelacaoPedidoBebida(Database):
    def __init__(self):
        super().__init__()
        
    def post(self, ped_beb):
        query = """
        INSERT INTO RelacaoPedidoBebida (id_ped, id_beb)
        VALUES (?, ?);
        """
        self.execute(query, ped_beb)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM RelacaoPedidoBebida
        WHERE id_ped_beb = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()

    def create_table(self):
        self.execute("""CREATE TABLE IF NOT EXISTS RelacaoPedidoBebida (
                                id_ped_beb  INTEGER PRIMARY KEY,
                                id_ped      INTEGER REFERENCES Pedido (id_ped),
                                id_beb      INTEGER REFERENCES Bebida (id_beb)
                        );
                     """)
        
class Bebida(Database):
    def __init__(self):
        super().__init__()

    def post(self, beb):
        query = """
        INSERT INTO Bebida (nome, alcoolica, descricao, volume, preco)
        VALUES (?, ?, ?, ?, ?);
        """
        self.execute(query, beb)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Bebida
        WHERE id_beb = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()

    def get_all(self):
        query = """
        SELECT * FROM Bebida
        """
        self.execute(query)
        return self.cur.fetchall()

    def create_table(self):
        self.execute("""CREATE TABLE IF NOT EXISTS Bebida (
                                id_beb      INTEGER PRIMARY KEY,
                                nome        TEXT NOT NULL,
                                alcoolica   BOOLEAN NOT NULL,
                                descricao   TEXT NOT NULL,
                                volume      TEXT NOT NULL,
                                preco       REAL NOT NULL
                        );
                     """)
