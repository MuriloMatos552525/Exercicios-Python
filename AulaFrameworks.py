'''
Metodo frameworks() ex1:

lista_chaves = ['chave1', 'chave2', 'chave3']
valor = 0

dici = dict. fromkeys(lista_chaves, valor)

ex2:

def teste(a, b, c):
print(f'a:{a} / b:{b} / c{c}')

lista = [1, 'banana', True]
teste(lista[0], lista[1], lista[3]) #parametro manual#
    a1 = 1
    a2 = 2
    a3 = 3
    teste(a1, a2, a3)
    teste(*lista)

'''

def teste(n, s):
    n = n + 2
    s[0] = s[0] + 1
    return

n1 = 1
lista = [1]

teste(n1, lista)
print('fim')