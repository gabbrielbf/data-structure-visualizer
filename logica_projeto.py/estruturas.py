# estrutura dos dados
from menu import menu_numerado, limpar_tela
from classes import pilhas_ou_filas

def adicionar_elemento():
    """ função global para adicionar elementos 
    independente do tipo de lista """

    while True:
        entrada = input('Qual elemento deseja adicionar: ')
        if entrada == '' or not entrada.strip():
            print('\n[ERRO] Espaços vazios não são permitidos!\n')
            continue
        else:
            print(f'O elemento [{entrada}] foi adicionado ✔️\n')
            break

    return entrada

def remover_elemento():

    retorno = pilha_ou_fila.selecionar_pilhas_ou_filas()

    if retorno == 1:
        print('Pilha (LIFO – Last In, First Out / O último que entra é o primeiro a sair)')
        if lista_pilhas:
            print(f'Removemos o último item: {lista_pilhas[-1]}')
            lista_pilhas.pop()
        else:
            print('A pilha está vazia!')
    else:
        print('Fila (FIFO – First In, First Out / O primeiro que entra é o primeiro a sair)')
        if lista_filas:
            print(f'Removemos o primeiro item: {lista_filas[0]}')
            lista_filas.pop(0)
        else:
            print('A fila está vazia!')

    return

lista_pilhas = []
lista_filas = []
pilha_ou_fila = pilhas_ou_filas()

def rodar_programa():

    while True:
        limpar_tela()
        opcao = menu_numerado()
        match opcao:
            case 1:
                
                pilha_ou_fila.exibir_pilhas_ou_filas()
                retorno = pilha_ou_fila.selecionar_pilhas_ou_filas()
                elemento = adicionar_elemento()

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

rodar_programa()