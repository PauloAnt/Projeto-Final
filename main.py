from EnviaDados import arvoreJogos
from time import sleep

Jogos = arvoreJogos()     

def cor_azul(texto):
    return f"\033[94m{texto}\033[0m"

def cor_verde(texto):
    return f"\033[42m{texto}\033[0m"

def cor_vermelha(texto):
    return f"\033[91m{texto}\033[0m"


#Menu
while True:
    try:
        print(f'''
================ Menu Principal ===============
{cor_azul("l")} Listar os jogos por sistema operacional
(p) Pesquisar jogo
{cor_verde("d")} Listar jogos por ano de lançamento
{cor_vermelha("s")} Sair                       

''')

        resposta = input("Opção: ").lower()
        
        if (resposta == "l"):
            continue    
            
        elif (resposta == "p"):
            continue

        elif (resposta == "d"):
            continue

        elif (resposta == "s"):
            print("Finalizando o programa...")
            sleep(1)
            break
        
        else:
            print("Opção inexistente!")
    # except AssertionError as ae:
    #     print(ae)
    # except BaseException as be:
    #     print(f"Erro desconhecido! '{be}'")
    except:
        print("Erro desconhecido, iremos tratar em breve!")