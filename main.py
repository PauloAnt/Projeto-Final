from BinarySearchTree import BinarySearchTree
from Jogo import Jogo

ignorar_primeiro = False

with open("computer_games.csv", "r", encoding="utf-8") as ds:
    for linha in ds.readlines():
        if (ignorar_primeiro == False):
            ignorar_primeiro = True
        else:
            linha_formatada = linha.split(",")
            data = linha_formatada[6][-2:].strip() + "/" + linha_formatada[6][1:-3] + "/" + linha_formatada[7][:5].strip()
            print(linha_formatada, data)