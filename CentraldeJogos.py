from BinarySearchTree import BinarySearchTree
from Jogo import Jogo

class CentralDeJogos():
    def __init__(self, arvore:BinarySearchTree):
        self.__arvore = arvore

    def find_all_names_game(self, key):
        
        return
    
    def search_in_central(self, key):
        pesquisar_jogo = Jogo(key)
        if (self.__arvore.search(pesquisar_jogo) == None):
            return f"Esse jogo não existe!"
        else:
            return self.__arvore.search(pesquisar_jogo)

    #Adicionar outros métodos
