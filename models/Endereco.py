from models import Database


class Endereco(Database):
    def __init__(self):
        super().__init__()
        
    def post(self, end):
        query = """
        INSERT INTO Endereco (id_cli, numero, rua, cidade, bairro)
        VALUES (?, ?, ?, ?, ?);
        """
        self.execute(query, end)
        self.commit()
        return "Ok"

    def get_by_id(self, id):
        query = """
        SELECT * FROM Endereco
        WHERE id_end = ?
        """
        self.execute(query, id)
        return self.cur.fetchone()

    def get_by_client(self, id_cli):
        query = """
        SELECT * FROM Endereco
        WHERE id_cli = ?
        """
        self.execute(query, id_cli)
        return self.cur.fetchall()
    
    def create_table(self):
        self.execute("""CREATE TABLE  IF NOT EXISTS Endereco (
                                id_end  INTEGER PRIMARY KEY,
                                id_cli  INTEGER REFERENCES Cliente (id_cli),
                                numero  INTEGER  NOT NULL,
                                rua     TEXT NOT NULL,
                                cidade  TEXT NOT NULL,
                                bairro  TEXT NOT NULL
                        );
                     """)
