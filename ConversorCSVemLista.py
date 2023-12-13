def converte_csv_em_lista(filename)-> list: 
    ignorar_primeiro = False
    dados = []

    with open(filename, "r", encoding="utf-8") as ds:
        for linha in ds.readlines():
            if ignorar_primeiro == False:
                ignorar_primeiro = True
            else:
                item = formata_linha(linha, ",", 5)
                dados.append(item)
    return dados

def formata_linha(linha:str, sep:str, ind:int)-> list:
    '''
    Retorna uma lista com todas as informações do jogo com as devidas adaptações.
    Recebe como parâmetro a frase, o separador de cada coluna e o índice identificando a posição
    da data para que ela esteja no formato XX/XX/XXXX
    '''
    info = []
    ignorar_proximo = []   
    aux = ''               
    linha_formatada = linha.split(sep)

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
    info[ind] = formata_data(info[ind], " ")
    return info

def formata_data(data:str, sep:str)->str:
    '''
    Recebe a data e o separador.
    Retorna a data com o formato XX/XX/XXXX.
    Não funciona com qualquer data, apenas com um formato mais específico!
    '''
    meses = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}
    separa_data = data.split()
    if (len(separa_data) == 1):
        data_formatada = "XX" + "/" + "XX" + "/" + separa_data[0]
    elif (len(separa_data) == 2):
        data_formatada = "XX" + "/" + meses[separa_data[0]] + "/" + separa_data[1]
    else:
        data_formatada = separa_data[1] + "/" + meses[separa_data[0]] + "/" + separa_data[2]
    return data_formatada

# lista_nome_jogos = []
# cont_SO = {}
# anos = {}
# cont_descartados = 0
# print(f"Quantidade de itens carregados: {len(dados)}\n")
#     print(f"Quantidade de itens descartados: {cont_descartados}\n")
#     print(f"Sistema Operacional mais popular: {max(cont_SO, key=cont_SO.get)}\n")

#     print("Quantidade de jogos lançados em cada ano:")
#     for chave, valor in sorted(anos.items()):
#         print(f'{chave}: {valor} jogo(s)')
# if (len(info) > 0):
#         if (info[0] not in lista_nome_jogos):
#             lista_nome_jogos.append(info[0])
#             for i in info[4].split():
#                 if (i not in cont_SO):
#                     cont_SO[i] = 1
#                 else:
#                     if (cont_SO == "Microsoft"):
#                         cont_SO["Windows"] += 1
#                     else:
#                         cont_SO[i] += 1
#             jogo = Jogo(info[0], info[1], info[2], info[3], info[4], data_formatada)
#             dados.add(jogo)
#             info = []
#             ignorar_proximo = []
#         else:
#             info = []
#             ignorar_proximo = []
#     else:
#         info = []
#         ignorar_proximo = []
#         cont_descartados += 1