from . import Database

class RelacaoPedidoPizza(Database):
    def __init__(self):
        super().__init__()
        
    def post(self, relacao):
        query = """
        INSERT INTO RelacaoPedidoPizza (id_ped, id_piz)
        VALUES (?, ?);
        """
        self.execute(query, relacao)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM RelacaoPedidoPizza
        WHERE id_ped_piz = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()
    
    def create_table(self):
        self.execute("""CREATE TABLE  IF NOT EXISTS RelacaoPedidoPizza (
                                id_ped_piz  INTEGER PRIMARY KEY,
                                id_ped      INTEGER REFERENCES Pedido (id_ped),
                                id_piz      INTEGER REFERENCES Pizza (id_piz)
                        );
                     """)

class Pizza(Database):
    def __init__(self):
        super().__init__()

    def post(self, pizza):
        query = """
        INSERT INTO Pizza (id_ped, id_tam, id_tipo, id_bor, preco)
        VALUES (?, ?, ?, ?, ?);
        """
        self.execute(query, pizza)
        self.commit()
        return "Ok"

    def get_by_pedido(self, id_ped):
        query = """
        SELECT * FROM Pizza
        WHERE id_ped = ?
        """
        self.execute(query, id_ped)
        return self.cur.fetchall()

    def create_table(self):
        self.execute("""CREATE TABLE IF NOT EXISTS Pizza (
                                id_piz  INTEGER PRIMARY KEY,
                                id_ped  INTEGER REFERENCES Pedido (id_ped),
                                id_tam  INTEGER REFERENCES Tamanho (id_tam),
                                id_tipo INTEGER REFERENCES Tipo (id_tipo),
                                id_bor  INTEGER REFERENCES Borda (id_bor),
                                preco   REAL NOT NULL
                        );
                     """)


class Sabor(Database):
    def __init__(self):
        super().__init__()

    def post(self, sabor):
        query = """
        INSERT INTO Sabor (id_tipo, nome, descricao)
        VALUES (?, ?, ?);
        """
        self.execute(query, sabor)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Sabor
        WHERE id_sab = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()

    def get_all(self):
        query = """
        SELECT * FROM Sabor
        """
        self.execute(query)
        return self.cur.fetchall()

    def create_table(self):
        self.execute("""CREATE TABLE  IF NOT EXISTS Sabor (
                                id_sab      INTEGER PRIMARY KEY,
                                id_tipo     INTEGER REFERENCES Tipo (id_tipo),
                                nome        TEXT NOT NULL,
                                descricao   TEXT NOT NULL
                        );
                     """)
        
class Borda(Database):
    def __init__(self):
        super().__init__()
        
    def post(self, borda):
        query = """
        INSERT INTO Borda (nome, descricao, preco)
        VALUES (?, ?, ?);
        """
        self.execute(query, borda)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Borda
        WHERE id_bor = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()
    
    def get_all(self):
        query = """
        SELECT * FROM Borda
        """
        self.execute(query)
        return self.cur.fetchall()
    
    def create_table(self):
        self.execute("""CREATE TABLE  IF NOT EXISTS Borda (
                                id_bor      INTEGER PRIMARY KEY,
                                nome        TEXT NOT NULL,
                                descricao   TEXT NOT NULL,
                                preco       REAL NOT NULL
                        );
                     """)

class Tipo(Database):
    def __init__(self):
        super().__init__()
        
    def post(self, tipo):
        query = """
        INSERT INTO Tipo (nome, preco)
        VALUES (?, ?);
        """
        self.execute(query, tipo)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Tipo
        WHERE id_tipo = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()
    
    def create_table(self):
        self.execute("""CREATE TABLE  IF NOT EXISTS Tipo (
                                id_tipo     INTEGER PRIMARY KEY,
                                nome        TEXT NOT NULL,
                                preco       REAL NOT NULL
                        );
                     """)
        
class Tamanho(Database):
    def __init__(self):
        super().__init__()
        
    def post(self, tam):
        query = """
        INSERT INTO Tamanho (nome, descricao, modificador, num_sabores)
        VALUES (?, ?, ?, ?);
        """
        self.execute(query, tam)
        self.commit()
        return "Ok"

    def get(self, id):
        query = """
        SELECT * FROM Tamanho
        WHERE id_tam = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()

    def get_all(self):
        query = """
        SELECT * FROM Tamanho
        """
        self.execute(query)
        return self.cur.fetchall()
    
    def create_table(self):
        self.execute("""CREATE TABLE  IF NOT EXISTS Tamanho (
                                id_tam      INTEGER PRIMARY KEY,
                                nome        TEXT NOT NULL,
                                descricao   TEXT NOT NULL,
                                modificador REAL NOT NULL,
                                num_sabores REAL NOT NULL
                        );
                     """)
