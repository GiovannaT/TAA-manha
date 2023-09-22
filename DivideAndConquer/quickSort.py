def particao(A, esquerda, direita):
    pivo = A[esquerda]
    
    i = esquerda
    j = direita
    
    while i <= j:
        while A[i] <= pivo:
            i += 1
            if i == direita:
                break
        
        while pivo <= A[j]:
            j -= 1
            if j == esquerda:
                break
        
        if i >= j:
            break
        
        A[i], A[j] = A[j], A[i]
    
    A[esquerda], A[j] = A[j], A[esquerda]
    
    return j

def quickSort(A, esquerda, direita):
    if esquerda < direita:
        indice_pivo = particao(A, esquerda, direita)
        
        quickSort(A, esquerda, indice_pivo - 1)
        quickSort(A, indice_pivo + 1, direita)

lista = [4, 7, 2, 1, 9, 8, -5]
quickSort(lista, 0, len(lista) - 1)
print(lista)