from Fila import Fila, FilaException

class HistorySearchException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class HistorySearch:
    def __init__(self):
        self.__search_fila = Fila(4)
    
    def add_search(self, search):
        self.__search_fila.enfileirar(search)

    def remove_search(self):
        if self.__search_fila.estaVazia():
            self.__search_fila.desenfileirar()

    def get_search_history(self):
        return self.__search.fila
