
from BinarySearchTree import BinarySearchTree
from Jogo import Jogo
from EnviaDados import arvoreJogos
from time import sleep

Jogos = arvoreJogos()     
#Menu

def cor_azul(texto):
    return f"\033[94m{texto}\033[0m"

def cor_verde(texto):
    return f"\033[42m{texto}\033[0m"

def cor_vermelha(texto):
    return f"\033[91m{texto}\033[0m"

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
            print(f"Resultado (SO): {Jogo.sistema}")
            
    #            print(f" Jogo           Gênero          Desenvolvedor")
            
            #Aqui deve ser mostrado os jogos na determinada ordem |  Gênero do jogo | Desenvolvedor dos jogo
            
            continue    
        
        elif (resposta == "p"):
            print(f"Tipo de busca: (l) Ocorrência da palavra: {}")
            print(f"Jogo: {Jogo.nome}")

    #            print(f" Jogo           Gênero          Desenvolvedor")
            
            #Deve conter os jogos que contenham o nome ou parte do nome iguais | Gênero do jogo | Desenvolvedor dos jogos
            continue

        elif (resposta == "d"):
            print("##Listando jogos por ano##")
            ano = int(input("Digite o ano para que seja exibido os jogos:"))
            if (ano == Jogo.data):
    #            print(f" Jogo           Gênero          Desenvolvedor")
                print(f"{Jogo.nome}, {Jogo.genero}, {Jogo.desenvolvedor}")

        elif (resposta == "s"):
            print("Finalizando o programa...")
            sleep(1)
            break
    
    # except AssertionError as ae:
    #     print(ae)
    # except BaseException as be:
    #     print(f"Erro desconhecido! '{be}'")
    # except:
    #     print("Erro desconhecido, iremos tratar em breve!")
