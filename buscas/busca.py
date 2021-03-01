''' Procura por elementos duplicados '''

def duplicate_elements(arr):
    for i in range(len(arr)-1):
        for j in  range(i+1, len(arr)-1):
            if arr[i] == arr[j]:
                return True
    return False

# Complexidade de Tempo
''' N-1 + N-2 + N-3 +... =       
    N * (N - 1) / 2 + 1 =
    (N ^ 2 - N) / 2 + 1 =
    O(N^2)
'''


''' Busca Linear em Lista de Alocação Sequencial '''

def search(arr, elem):
    #Retorna o indice do elemento se ele 
    #estiver na lista, ou None, caso não esteja
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return None