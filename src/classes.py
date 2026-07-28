from abc import ABC, abstractmethod

class EstruturaDeDados(ABC):
    """ classe separada para definir o tipo de lista a ser trabalhada """

    def __init__(self):
        self._itens = [] # <- iniciando uma lista vazia na classe pai para que as filhas apenas implementem o modo de lidar com sua respectiva lista
        return

    def exibir_itens(self):
        """ método global de exibição dos itens pois 
        ambas as listas usam a mesma lógica para exibir seus elementos"""

        if self._itens:
            print(f'\nExibindo a lista de {self.__class__.__name__}:') # <- essa linha exibe em tempo real o nome da lista a ser manipulada
            print('-'*30)
            for indice, item in enumerate(self._itens, start=1):
                print(f'{indice} - {item} ({type(item).__name__})') # <- exibindo a posição, item e o tipo de dado do item adicionado
            print('-'*30)
        else:
            print(f'\nA lista de {self.__class__.__name__} está vazia!\n')

    @abstractmethod
    def adicionar_item(self, item):
        """ método global para adicionar elementos 
            independente do tipo de lista """
        pass

    @abstractmethod
    def remover_item(self):
        """ método responsável pela remoção dos itens gerais, independente se é PILHA ou FILA pois 
        o que definirá a remoção será o a própria classe em si instânciada no programa procedual """
        pass


class Pilhas(EstruturaDeDados):

    def adicionar_item(self, item):
        self._itens.append(item)
        return 

    def remover_item(self):
        if self._itens:
            print('-'*30)
            print('Pilha (LIFO – Last In, First Out / O último que entra é o primeiro a sair)')
            print(f'Removemos o último item: {self._itens[-1]}')
            print('-'*30)
            self._itens.pop()
        else:
            print(f'\nA lista de {self.__class__.__name__} está vazia!\n')
        return 


class Filas(EstruturaDeDados):

    def adicionar_item(self, item):
        self._itens.append(item)
        return 

    def remover_item(self):
        if self._itens:
            print('-'*30)
            print('Fila (FIFO – First In, First Out / O primeiro que entra é o primeiro a sair)')
            print(f'Removemos o primeiro item: {self._itens[0]}')
            print('-'*30)
            self._itens.pop(0)
        else:
            print(f'\nA lista de {self.__class__.__name__} está vazia!\n')
        return 
