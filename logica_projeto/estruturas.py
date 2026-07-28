# estrutura dos dados
from .menu import menu_numerado, limpar_tela, exibir_pilhas_ou_filas, selecionar_pilhas_ou_filas, retornar_formatado # { usamos um "." depois do "from" para conseguir importar essas funções e métodos
from .classes import Pilhas, Filas # para o arquivo "main" e assim fazer com que ele funcione 
from .lessons import * # } da forma mais enxuta possível, exibindo ao usuário somente o que é necessário

import time
import sys

def obter_elemento(estrutura):
    """ Função criada apenas para deixar o 
    médodo 1 da função "run_code" mais "enxuto" """

    while True:
        entrada = input('Qual elemento deseja adicionar: ')
        if entrada == '' or not entrada.strip(): # <- Bloco responsável por evitar que o usuário introduza espaços vazios na lista
            print('\n[ERRO] Espaços vazios não são permitidos!\n')
            continue
        else:
            nome_estrutura = estrutura.__class__.__name__ # <- essa variável serve apenas para fazer uma exibição de nome dinâmica 
            print(f'\nO elemento [{entrada}] foi adicionado a lista de {nome_estrutura} ✔️\n') # ao usuáro sobre qual lista estamos manipulando
            break

    return entrada

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

    return

def encerrar_programa():
    """ função que encerra (ou não) o programa de 
    acordo com uma interação do usuário """

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
    """ função designada a selecionar o fluxo de manipulação das listas entre pilhas ou 
    filas somente uma vez, tirando a necessidade de escolher sempre qual lista manipular """

    estrutura_atual = None
    
    exibir_pilhas_ou_filas()
    opcao = selecionar_pilhas_ou_filas() # <- seleciona qual lista manipular dentre PILHAS ou FILAS

    if opcao == 1: # <- CASO 1 - PILHAS
        estrutura_atual = Pilhas()
    else: # OUTRO CASO, NO CASO 2 - FILAS
        estrutura_atual = Filas()

    nome_formatado = retornar_formatado(opcao)

    print('-'*30)
    print(f'Iremos trabalhar com {nome_formatado}')

    return estrutura_atual

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
                elemento = obter_elemento(estrutura_atual)
                estrutura_atual.adicionar_item(elemento)
            case 2 :
                estrutura_atual.remover_item()
            case 3:
                estrutura_atual.exibir_itens()
            case 4:
                pass
            case 5:
                if encerrar_programa() == True:
                    break
                else:
                    continue

    return