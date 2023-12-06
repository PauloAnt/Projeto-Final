from ConversorCSVemArvore import converte_csv_em_arvore
from CentraldeJogos import CentralDeJogos
from time import sleep
from HistoricoSearch import HistorySearch, HistorySearchException

jogos = converte_csv_em_arvore("computer_games.csv")
gamer_center = CentralDeJogos(jogos)

def cor_azul(texto):
    return f"\033[94m{texto}\033[0m"

def cor_vermelha(texto):
    return f"\033[91m{texto}\033[0m"

#Menu
while True:
    try:
        print(f'''
{cor_vermelha("================ Menu Principal ===============")} 
{cor_azul("(p)")} Pesquisar jogo
{cor_azul("(l)")} Listar os jogos por sistema operacional
{cor_azul("(d)")} Listar jogos por ano de lançamento
{cor_azul("(s)")} Sair                      
''')

# Colocar o histórico de pesquisa ao lado do menu principal, o histórico vai conter as últimas quatro pesquisas feitas pelo usuário
# Colocar Pilha

        resposta = input("Opção: ")
            
        if (resposta == "p"):
            pesquisa = input("Pesquisar: ")
            print(gamer_center.search_in_central(pesquisa))
            sleep(2)

        elif (resposta == "l"):
            continue

        elif (resposta == "d"):
            continue

        elif (resposta == "s"):
            print("Finalizando o programa...")
            sleep(1)
            break
        
        else:
            print("Opção inexistente!")
    except AssertionError as ae:
        print(ae)
    # except BaseException as be:
    except:
        print("Erro desconhecido, iremos tratar em breve!")