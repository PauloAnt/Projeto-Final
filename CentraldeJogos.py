from BinarySearchTree import BinarySearchTree
from Jogo import Jogo

class CentralDeJogos():
    def __init__(self):
        self.__tree = BinarySearchTree()

    def addGame(self, jogo:Jogo):
        self.__tree.add(jogo)

    def find_game_year(self):
        pass
    
    def find_game_SO(self):
        pass

    def search_game(self, key):
        pesquisar_jogo = Jogo(key)
        if (self.__tree.search(pesquisar_jogo) == None):
            return f"Esse jogo não existe!"
        else:
            return self.__tree.search(pesquisar_jogo)

