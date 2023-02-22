CREATE TABLE Cliente (
    id_cli      INTEGER PRIMARY KEY,
    nome        TEXT NOT NULL,
    telefone    TEXT NOT NULL,
    email       TEXT NOT NULL UNIQUE,
    hash_pass   TEXT NOT NULL
);

CREATE TABLE Endereco (
    id_end  INTEGER PRIMARY KEY,
    id_cli  INTEGER REFERENCES Cliente (id_cli),
    numero  INTEGER  NOT NULL,
    rua     TEXT NOT NULL,
    cidade  TEXT NOT NULL,
    bairro  TEXT NOT NULL
);

CREATE TABLE Entregador (
    id_ent  INTEGER PRIMARY KEY,
    nome    TEXT NOT NULL,
    placa   TEXT NOT NULL
);

CREATE TABLE Pedido (
    id_ped  INTEGER PRIMARY KEY,
    id_cli  INTEGER REFERENCES Cliente (id_cli),
    id_end  INTEGER REFERENCES Endereco (id_end),
    id_ent  INTEGER REFERENCES Entregador (id_ent),
    data    DATE NOT NULL,
    estado  TEXT NOT NULL,
    entrega REAL NOT NULL,
    total   REAL NOT NULL
);

CREATE TABLE RelacaoPedidoPizza (
    id_ped_piz  INTEGER PRIMARY KEY,
    id_ped      INTEGER REFERENCES Pedido (id_ped),
    id_piz      INTEGER REFERENCES Pizza (id_piz)
);

CREATE TABLE Pizza (
    id_piz  INTEGER PRIMARY KEY,
    id_ped  INTEGER REFERENCES Pedido (id_ped),
    id_tam  INTEGER REFERENCES Tamanho (id_tam),
    id_tipo INTEGER REFERENCES Tipo (id_tipo),
    id_bor  INTEGER REFERENCES Borda (id_bor),
    preco   REAL NOT NULL
);

CREATE TABLE RelacaoPizzaSabor (
    id_piz_sab  INTEGER PRIMARY KEY,
    id_piz      INTEGER REFERENCES Pizza (id_piz),
    id_sab      INTEGER REFERENCES Sabor (id_sab)
);

CREATE TABLE Sabor (
    id_sab      INTEGER PRIMARY KEY,
    id_tipo     INTEGER REFERENCES Tipo (id_tipo),
    nome        TEXT NOT NULL,
    descricao   TEXT NOT NULL
);

CREATE TABLE Borda (
    id_bor      INTEGER PRIMARY KEY,
    nome        TEXT NOT NULL,
    descricao   TEXT NOT NULL,
    preco   REAL NOT NULL
);

CREATE TABLE Tipo (
    id_tipo      INTEGER PRIMARY KEY,
    nome        TEXT NOT NULL,
    preco   REAL NOT NULL
);

CREATE TABLE Tamanho (
    id_tam      INTEGER PRIMARY KEY,
    nome        TEXT NOT NULL,
    descricao   TEXT NOT NULL,
    modificador REAL NOT NULL,
    num_sabores REAL NOT NULL
);

CREATE TABLE RelacaoPedidoBebida (
    id_ped_beb  INTEGER PRIMARY KEY,
    id_ped      INTEGER REFERENCES Pedido (id_ped),
    id_beb      INTEGER REFERENCES Bebida (id_beb)
);

CREATE TABLE Bebida (
    id_beb      INTEGER PRIMARY KEY,
    nome        TEXT NOT NULL,
    alcoolica   BOOLEAN NOT NULL,
    descricao   TEXT NOT NULL,
    volume      TEXT NOT NULL,
    preco       REAL NOT NULL
);
