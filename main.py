from ConversorCSVemLista import converte_csv_em_lista
from CentraldeJogos import CentralDeJogos
from Jogo import Jogo
from time import sleep
from HistoricoSearch import HistorySearch, HistorySearchException

def cor_azul(texto):
    return f"\033[94m{texto}\033[0m"

def cor_vermelha(texto):
    return f"\033[91m{texto}\033[0m"

jogos = converte_csv_em_lista("computer_games.csv")
gamer_center = CentralDeJogos()

for item in jogos:
    game = Jogo(item[0], item[1], item[2], item[3], item[4], item[5])
    gamer_center.addGame(game)

#Menu
while True:
    try:
        print(f'''
{cor_vermelha("================ Menu Principal ===============")} 
{cor_azul("(p)")} Pesquisar jogo.
{cor_azul("(l)")} Listar os jogos por sistema operacional.
{cor_azul("(d)")} Listar jogos por ano de lançamento.
{cor_azul("(s)")} Sair.                 
''')

        resposta = input("Opção: ")
            
        if (resposta == "p"):
            pesquisa = input("Pesquisar: ").lower()
            print(gamer_center.search_game(pesquisa))
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
    except BaseException as be:
        print(be, "Erro desconhecido, iremos tratar em breve!")