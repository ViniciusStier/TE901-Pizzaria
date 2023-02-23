import os
from models.Bebida import Bebida
from models.Entregador import Entregador
from models.Pizza import Borda, Sabor, Tamanho, Tipo

loop = True
while loop:
    os.system("clear")
    menu_str = """
        1) Cadastrar entregador.
        2) Cadastrar Bebida
        3) Cadastrar Sabor de pizza
        4) Cadastrar Tipos de pizza
        5) Cadastrar Bordas de pizza
        6) Cadastrar Tamanhos de pizza
        10) Sair
    escolha a opçao:"""
    escolha = int(input(menu_str))
    if escolha == 1:
        ent = Entregador()
        nm = input("Nome:")
        plc = input("Placa:")
        ent.post([nm, plc])
        print(f"{nm} foi cadastrado.")
    if escolha == 2:
        ent = Bebida()
        nm = input("Nome:")
        alc = bool(input("Alcoolica:"))
        des = input("Descrição:")
        vol = input("Volume:")
        plc = input("Preço:")
        ent.post([nm, alc, des, vol, plc])
        print(f"{nm} foi cadastrado.")
    elif escolha == 4:
        ent = Tipo()
        nm = input("Nome:")
        plc = input("Preço:")
        ent.post([nm, float(plc)])
        print(f"{nm} foi cadastrado.")
    elif escolha == 5:
        ent = Borda()
        nm = input("Nome:")
        des = input("Descrição:")
        plc = input("Preço:")
        ent.post([nm, des, float(plc)])
        print(f"{nm} foi cadastrado.")
    elif escolha == 6:
        ent = Tamanho()
        nm = input("Nome:")
        des = input("Descrição:")
        plc = input("Modificador:")
        sab = input("Nº de sabores:")
        ent.post([nm, des, float(plc), sab])
        print(f"{nm} foi cadastrado.")
    elif escolha == 10:
        loop = False
    


os.system("clear")
