# Merge Sort - ordenação por intercalação (mistura)
# Complexidade: O(n*log(n));

def merge_sort(lita):
    if len(lista)>1:
        #meio da lista#
        meio = len(lista) // 2
        
        #dividindo a lista em duas - fatiamento de lista#
        esquerda = lista[:meio] # esquerdo do meio pra metade
        direita = lista[meio:] # direito do meio pra frente
        # chamada recursiva
        merge_sort(esquerda)# chama o metodo para os elementos da esquerda
        merge_sort(direita)

        #variaveis
        #i - fará o controle da lista esquerda#
        #j - fará o controle da lista direita#
        #k - fará o controle da lista anterior a recursao#
        i = j = k = 0
        while i < len(esquerda) and j<len(direita):
            if esquerda[i]<direita[j]:
                lista[k] = esquerda[i]
                i+=1
            else:
                lista[k] = direita[j]
                j+=1 
            k+=1

        