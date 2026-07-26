# estrutura dos dados
from .menu import menu_numerado, limpar_tela # { usamos um "." depois do "from" para conseguir importar essas funções e métodos
from .classes import PilhasOuFilas # para o arquivo "main" e assim fazer com que ele funcione 
from .lessons import * # } da forma mais enxuta possível, exibindo ao usuário somente o que é necessário

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

    pilha_ou_fila.exibir_pilhas_ou_filas()
    retorno = pilha_ou_fila.selecionar_pilhas_ou_filas()
    pilha_e_fila = pilha_ou_fila.retornar_formatado()

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

    pilha_ou_fila.exibir_pilhas_ou_filas()
    retorno = pilha_ou_fila.selecionar_pilhas_ou_filas()
    pilha_e_fila = pilha_ou_fila.retornar_formatado()

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

lista_pilhas = []
lista_filas = []
pilha_ou_fila = PilhasOuFilas()

def run_code():
    """ função responsável por pegar todas as funções definidas acima e fazê-las funcionar em conjunto com
    um bloco de código que define o caminho do usuário atráves de decisões tomadas com base no "menu_enumerado" """

    print(BANNER) # { esse bloco tem como finalidade dar uma conceituada ao usuário sobre a ideia e funcionamento por trás
    print(INTRO_TEXTO)
    limpar_tela()
    print(TEORIA_PILHA)
    print(DIVISOR)
    print(TEORIA_FILA) # } da lógica das PILHAS e FILAS na programação em geral.

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