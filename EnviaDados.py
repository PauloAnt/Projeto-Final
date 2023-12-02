from BinarySearchTree import BinarySearchTree
from Jogo import Jogo

ignorar_primeiro = False
ignorar_proximo = False
info = []
dados = BinarySearchTree()

#Falta terminar as formatações
#Passando os dados do dataset para a estrutura de dados
def arvoreJogos():
    with open("computer_games.csv", "r", encoding="utf-8") as ds:
        for linha in ds.readlines():
            if (ignorar_primeiro == False):
                ignorar_primeiro = True
            else:
                linha_formatada = linha.split(",")
                for i in range(len(linha_formatada)):
                    if (ignorar_proximo == True):
                        ignorar_proximo = False

                    elif (linha_formatada[i][0] == '"'):
                        aux = linha_formatada[i] + linha_formatada[i + 1]
                        formato = aux.strip('"').rstrip("\n").strip('"')
                        info.append(formato)
                        ignorar_proximo = True
                    
                    else:
                        formato = linha_formatada[i].strip('"').rstrip("\n").strip('"')
                        info.append(formato)
                
                jogo = Jogo(info[0], info[1], info[2], info[3], info[4], info[5])
                print(jogo)
                dados.add(jogo)
                info = []
    return dados