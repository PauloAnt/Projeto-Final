from BinarySearchTree import BinarySearchTree
from Jogo import Jogo

def converte_csv_em_arvore(filename):
    
    lista_nome_jogos = []
    cont_SO = {}
    anos = {}
    meses = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6", "July": "7", "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}
    ignorar_primeiro = False
    
    ignorar_proximo = []
    info = []

    dados = BinarySearchTree()
    aux = '' 
    cont_descartados = 0

    with open(filename, "r", encoding="utf-8") as ds:
            for linha in ds.readlines():
                try:
                    if ignorar_primeiro == False:
                        ignorar_primeiro = True
                    else:

                        linha_formatada = linha.split(",")
                        for i in range(len(linha_formatada)):
                            if i in ignorar_proximo:
                                continue

                            elif linha_formatada[i][0] == '"':
                                for j in range(i, len(linha_formatada)):
                                    if linha_formatada[j][-1] == '"':
                                        ignorar_proximo.append(j)
                                        aux += linha_formatada[j]
                                        break
                                    else:
                                        ignorar_proximo.append(j)
                                        aux += linha_formatada[j]
                                formato = aux.strip('"').rstrip("\n").strip('"')
                                info.append(formato)
                                aux = ''
                            else:
                                formato = linha_formatada[i].strip('"').rstrip("\n").strip('"')
                                info.append(formato)
                        
                        separa_data = info[5].split()
                        if (len(separa_data) == 1):
                            data_formatada = "XX" + "/" + "XX" + "/" + separa_data[0]
                            if (separa_data[0] not in anos):
                                anos[separa_data[0]] = 1
                            else:
                                anos[separa_data[0]] += 1
                        elif (len(separa_data) == 2):
                            data_formatada = "XX" + "/" + meses[separa_data[0]] + "/" + separa_data[1]
                            if (separa_data[1] not in anos):
                                anos[separa_data[1]] = 1
                            else:
                                anos[separa_data[1]] += 1
                        else:
                            data_formatada = separa_data[1] + "/" + meses[separa_data[0]] + "/" + separa_data[2]
                            if (separa_data[2] not in anos):
                                anos[separa_data[2]] = 1
                            else:
                                anos[separa_data[2]] += 1

                        if (len(info) > 0):
                            if (info[0] not in lista_nome_jogos):
                                lista_nome_jogos.append(info[0])
                                for i in info[4].split():
                                    if (i not in cont_SO):
                                        cont_SO[i] = 1
                                    else:
                                        if (cont_SO == "Microsoft"):
                                            cont_SO["Windows"] += 1
                                        else:
                                            cont_SO[i] += 1
                                jogo = Jogo(info[0], info[1], info[2], info[3], info[4], data_formatada)
                                dados.add(jogo)
                                info = []
                                ignorar_proximo = []
                            else:
                                info = []
                                ignorar_proximo = []
                        else:
                            info = []
                            ignorar_proximo = []
                            cont_descartados += 1

                except RecursionError:
                    dados.balance()
                    continue

    print(f"Quantidade de itens carregados: {len(dados)}\n")
    print(f"Quantidade de itens descartados: {cont_descartados}\n")
    print(f"Sistema Operacional mais popular: {max(cont_SO, key=cont_SO.get)}\n")

    print("Quantidade de jogos lançados em cada ano:")
    for chave, valor in sorted(anos.items()):
        print(f'{chave}: {valor} jogo(s)')
    return dados

# Chamar a função e imprimir a árvore
tree = converte_csv_em_arvore("computer_games.csv")
