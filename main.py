
import sqlite3
import math
conexao = sqlite3.connect('pizzaria.db')

cursor = conexao.cursor()

print("Inserção de novo estudante do banco bib.db\n")
cli_nome = input("   Nome completo: ")
cli_phone = input("   Telefone: ")
cli_email = input("   Email: ")
cli_hash = "svndvlobds backp0-"

query = """
INSERT INTO Cliente (nome, telefone, email, hash_pass)
VALUES (?, ?, ?, ?);
"""

cursor.execute(query, (cli_nome, cli_phone, cli_email, cli_hash)) # passagem do nome e email para a montagem da query
# método executemany passa a query e uma lista de tuplas,
# cada tupla como os dados de uma operação de insert

# commit para persistir as inserções na base de dados
conexao.commit()
# insert, update e delete precisam do commit pois alteram a base de dados

cursor.close()
conexao.close()
