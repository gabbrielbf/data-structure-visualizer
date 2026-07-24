# estrutura dos dados
from menu import menu_numerado, limpar_tela
from classes import pilhas_ou_filas
from lessons import *

def adicionar_elemento():
    """ função global para adicionar elementos 
    independente do tipo de lista """

    pilha_ou_fila.exibir_pilhas_ou_filas()
    retorno, pilha_e_fila = pilha_ou_fila.selecionar_pilhas_ou_filas()

    while True:
        entrada = input('Qual elemento deseja adicionar: ')
        if entrada == '' or not entrada.strip():
            print('\n[ERRO] Espaços vazios não são permitidos!\n')
            continue
        else:
            print(f'\nO elemento [{entrada}] foi adicionado a lista de {pilha_e_fila} ✔️\n')
            break

    return entrada, retorno

def remover_elemento():

    pilha_ou_fila.exibir_pilhas_ou_filas()
    retorno, pilha_e_fila = pilha_ou_fila.selecionar_pilhas_ou_filas()

    if retorno == 1:
        print('\nPilha (LIFO – Last In, First Out / O último que entra é o primeiro a sair)')
        if lista_pilhas:
            print(f'Removemos o último item: {lista_pilhas[-1]}\n')
            lista_pilhas.pop()
        else:
            print(f'\nA lista de {pilha_e_fila} está vazia!\n')
    else:
        print('\nFila (FIFO – First In, First Out / O primeiro que entra é o primeiro a sair)')
        if lista_filas:
            print(f'Removemos o primeiro item: {lista_filas[0]}\n')
            lista_filas.pop(0)
        else:
            print(f'\nA lista de {pilha_e_fila} está vazia!\n')

    return

lista_pilhas = []
lista_filas = []
pilha_ou_fila = pilhas_ou_filas()

def run_code():

    print(BANNER)
    print(INTRO_TEXTO)
    limpar_tela()
    print(TEORIA_PILHA)
    print(DIVISOR)
    print(TEORIA_FILA)

    while True:
        limpar_tela()
        opcao = menu_numerado()
        match opcao:
            case 1:

                elemento, retorno = adicionar_elemento()

                if retorno == 1:
                    lista_pilhas.append(elemento)
                else:
                    lista_filas.append(elemento)

            case 2 :

                remover_elemento()

            case 3:
                pass

            case 4:
                print('\nprograma encerrado.\n')
                break

run_code()