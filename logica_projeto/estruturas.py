# estrutura dos dados
from .menu import menu_numerado, limpar_tela, exibir_pilhas_ou_filas, selecionar_pilhas_ou_filas, retornar_formatado # { usamos um "." depois do "from" para conseguir importar essas funções e métodos
from .classes import Pilha, Fila # para o arquivo "main" e assim fazer com que ele funcione 
from .lessons import * # } da forma mais enxuta possível, exibindo ao usuário somente o que é necessário

import time
import sys

def obter_elemento():
    """ Função criada apenas para deixar o 
    médodo 1 da função "run_code" mais "enxuto" """

    pilha_ou_fila.exibir_pilhas_ou_filas()
    retorno = pilha_ou_fila.selecionar_pilhas_ou_filas()
    pilha_e_fila = pilha_ou_fila.retornar_formatado()

    while True:
        entrada = input('Qual elemento deseja adicionar: ')
        if entrada == '' or not entrada.strip(): # <- Bloco responsável por evitar que o usuário introduza espaços vazios na lista
            print('\n[ERRO] Espaços vazios não são permitidos!\n')
            continue
        else:
            print(f'\nO elemento [{entrada}] foi adicionado a lista de {pilha_e_fila} ✔️\n')
            break

    return entrada, retorno

def lecionar_usuario():
    """ exibição dinâmica e animada para 
    imersão do usuário ao conteúdo """

    limpar_tela()
    print(DIVISOR) 
    for char in BANNER: # <- esse bloco exibe letra a letra do cabeçario
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
    print(DIVISOR)
    print(INTRO_TEXTO)

    limpar_tela()

    print(DIVISOR)
    for char in TEORIA_PILHA:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(DIVISOR)

    input('Press ENTER to continue...')

    print(DIVISOR)
    for char in TEORIA_FILA:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(DIVISOR)

    return

def adicionar_elemento(elemento, retorno):
    """ função global para adicionar elementos 
    independente do tipo de lista """

    if retorno == 1:
        lista_pilhas.append(elemento) # <- Joga na pilha se o retorno for 1
    else:
        lista_filas.append(elemento) # <- Joga na fila se for outro valor (no caso 2)
        
    return

def remover_elemento():
    """ função responsável pela remoção dos itens gerais, independente se é PILHA ou FILA pois o que definirá a remoção
    será o retorno da variavel "retorno" presente no método da classe "selecionar_pilhas_ou_filas" """

    if retorno == 1:
        if lista_pilhas:
            print('-'*30)
            print('Pilha (LIFO – Last In, First Out / O último que entra é o primeiro a sair)')
            print(f'Removemos o último item: {lista_pilhas[-1]}')
            print('-'*30)
            lista_pilhas.pop()
        else:
            print(f'\nA lista de {pilha_e_fila} está vazia!\n') # <- variável "pilha_e_fila" criada apenas para exibir dinâmicamente qual lista está
    else:                                                       # sendo manipulada em tempo real
        if lista_filas:
            print('-'*30)
            print('Fila (FIFO – First In, First Out / O primeiro que entra é o primeiro a sair)')
            print(f'Removemos o primeiro item: {lista_filas[0]}')
            print('-'*30)
            lista_filas.pop(0)
        else:
            print(f'\nA lista de {pilha_e_fila} está vazia!\n')

    return

def exibir_elementos():
    """ função responsável pela exibição dos itens
    gerais seguindo a mesma lógica da função de remoção """

    if retorno == 1:
        if lista_pilhas:
            print(f'\nExibindo a lista de {pilha_e_fila}:')
            print('-'*30)
            for indice, item in enumerate(lista_pilhas, start=1):
                print(f'{indice} - {item}')
            print('-'*30)
        else:
            print(f'\nA lista de {pilha_e_fila} está vazia!\n')
    else:
        if lista_filas:
            print(f'Exibindo a lista de {pilha_e_fila}:')
            print('-'*30)
            for indice, item in enumerate(lista_filas, start=1):
                print(f'{indice} - {item}')
            print('-'*30)
        else:
            print(f'\nA lista de {pilha_e_fila} está vazia!\n')

    return

def encerrar_programa():
    while True:
        try:
            
            certeza = str(input('Certeza que deseja encerrar?[S/N]: ')).lower()
            
            if certeza != 's' and certeza != 'n': # <- Confere se o usuário digitou algo diferente de S ou N
                print('\n[ERRO] Somente [S/N]!')
                continue

        except ValueError:
            print('\n[ERRO] Valor inválido.\n')
            continue
        break

    if certeza == 's':
        print('\nPrograma encerrado.\n') # <- ENCERRA
        return True
    
    elif certeza == 'n':
        print('\nEntão vamos voltar!\n') # <- VOLTA PARA O MENU
    
    return False

def definir_estrutura():
    """ função designada a selecionado o fluxo de manipulação das listas entre pilhas ou 
    filas somente uma vez, tirando a necessidade de escolher sempre qual lista manipular """

    estrutura_atual = None
    
    exibir_pilhas_ou_filas()
    opcao = selecionar_pilhas_ou_filas()

    if opcao == 1:
        estrutura_atual = Pilha()
    else:
        estrutura_atual = Fila()

    nome_formatado = retornar_formatado(opcao)

    print('-'*30)
    print(f'Iremos trabalhar com {nome_formatado}')

    return estrutura_atual

lista_pilhas = []
lista_filas = []

def run_code():
    """ função responsável por pegar todas as funções definidas acima e fazê-las funcionar em conjunto com
    um bloco de código que define o caminho do usuário atráves de decisões tomadas com base no "menu_enumerado" """

    lecionar_usuario()
    estrutura_atual = definir_estrutura()

    while True:

        limpar_tela()
        opcao = menu_numerado()

        match opcao:
            case 1:
                elemento, retorno = obter_elemento()
                adicionar_elemento(elemento, retorno)
            case 2 :
                remover_elemento()
            case 3:
                exibir_elementos()
            case 4:
                if encerrar_programa() == True:
                    break
                else:
                    continue
                
    return