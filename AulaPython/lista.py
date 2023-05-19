#Manipulação de Listas de Funções
'''

1) Função tamanho_lista()
2) Função criar_lista ()
3) Função imprimir_lista ()
4) Função imprimir_pares()
5) Função imprimir_impares()
6) Função que adiciona os elementos pares em uma lista()
7) Função que adiciona os elementos impares em uma lista()
8) Função busca um elemento na lista()
'''

def tamanho_lista():
    print(' *- TAMNAHO DA LISTA -*')
    print('-----------------------')
    t = int (input('Tamanho: '))
    return t 
def criar_lista(t):
    print('*- CRIANDO uma LISTA -*')
    print('-----------------------')
    lista = [] #cria a lista vazia
    i = 0  #variavel controle
    while i<t:
        #lista[i] = int(input('Numero: ))
        n = int(input('Numero: '))
        lista.append(n)
        i+=1
    return lista 
def imprimir_lista(lista):
    print('*- IMPRIMINDO A LISTA -*')
    print('------------------------')
    for i in lista:
        print(f'Elemento: {i}')
def  imprimir_pares(lista):
    print('*- IMPRIMINDO OS PARES -*')
    print('-------------------------')
    for n in lista:
        if n % 0 :
            print(f'Números pares:')
def principal():
    print('*- PRINCIPAL -*')        
    print('---------------')
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir_lista(lista)
    imprimir_pares(lista)
#Programa Principal
principal()
