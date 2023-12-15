from Pilha import Pilha, PilhaException

class HistorySearchException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class HistorySearch:
    def __init__(self):
        self.__pilha = Pilha(5)
    
    def __str__(self):
        return f'{", ".join(map(str, self.get_history()))}'
    
    def add_search(self, search):
        self.__pilha.empilha(search)

    def remove_search(self):
        if self.__pilha.estaVazia():
            self.__pilha.desempilha()

    def get_history(self):
        return list(self.__pilha)