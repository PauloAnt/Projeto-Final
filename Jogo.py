class Jogo():
    def __init__(self, nome, desenvolvedor, produtora, genero, sistema, data):
        self.__nome = nome
        self.__desenvolvedor = desenvolvedor
        self.__produtora = produtora
        self.__genero = genero
        self.__sistema = sistema
        self.__data = data

    @property
    def nome(self):
        return self.__nome
    @property
    def desenvolvedor(self):
        return self.__desenvolvedor
    @property
    def produtora(self):
        return self.__produtora
    @property
    def genero(self):
        return self.__genero
    @property
    def sistema(self):
        return self.__sistema
    @property
    def data(self):
        return self.__data