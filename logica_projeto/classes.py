from abc import ABC, abstractmethod

class EstruturaDeDados(ABC):
    """ classe separada para definir o tipo de lista a ser trabalhada """

    def __init__(self):
        self._itens = [] # iniciando uma lista vazia na classe pai para que as filhas apenas implementem o modo de lidar com sua respectiva lista
        return

    @abstractmethod
    def adicionar_item(self, item):
        pass

    @abstractmethod
    def remover_item(self):
        pass


class Pilha(EstruturaDeDados):
    pass


class Fila(EstruturaDeDados):
    pass