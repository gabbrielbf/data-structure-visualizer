from menu import ler_opcao_numerica

class pilhas_ou_filas:
    """ classe separada para definir o tipo de lista a ser trabalhada """

    def __init__(self):
        self.pilha_e_fila = None # { iniciando esses dois atributos no init para conseguir retornar eles com os métodos
        self.pilha_ou_fila = None # } abaixo sem precisar ficar reescrevendo-os
        return

    def exibir_pilhas_ou_filas(self):
        """ método responsável por apenas exibir qual será o tipo de lista a ser trabalhada """

        self.opcoes = ['Pilhas', 'Filas'] # <- lista criada apenas para exibição dinâmica
        
        print('\nCom o que deseja trabalhar:')
        print('-'*30)
        for indice, lista in enumerate(self.opcoes, start=1):
            print(f'{indice} - {lista}')
        print('-'*30)

        return

    def selecionar_pilhas_ou_filas(self):
        """ método responsável por retornar um valor numérico e trabalhar encima desse retorno """

        while True:
            self.pilha_ou_fila = ler_opcao_numerica()

            if (self.pilha_ou_fila < 1 or
                self.pilha_ou_fila > 2): # <- esse bloco de while true serve apenas para definir qual será o caminho traçado pelo usuário após
                print('[ERRO] opção não encontrada\n') # decidir qual opção dentre as opções, a partir daqui saberemos se ele quer trabalhar com pilhas ou filas
                continue
            else:
                break
            
        return self.pilha_ou_fila

    def retornar_formatado(self):
        """ método separada e "irrelevante" criada apenas 
        para retonar uma exibição formatada e dinâmica ao usuário """

        if self.pilha_ou_fila == 1:
            self.pilha_e_fila = 'Pilhas'
        else:   # <- esse bloco do else serve apenas para fazer uma exibição dinâmica no arquivo main
            self.pilha_e_fila = 'Filas'

        return self.pilha_e_fila