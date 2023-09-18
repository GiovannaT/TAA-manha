def mergeSort (lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:] 
    
    esquerda = mergeSort(esquerda)
    direita = mergeSort(direita)

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else: 
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


lista = [12, 11, 13, 5, 6, 7]
print("Lista original:", lista)
print("Lista ordenada:", mergeSort(lista))