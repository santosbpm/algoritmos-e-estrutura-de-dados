# Ordenação por inserção
def insertion_sort(arr):
    
    for j in range(1, len(arr)):
        key = arr[j]
        # Inserir arr[j] na sequência ordenada arr[1.. j - 1]
        i = j - 1
        
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
            
        arr[i+1] = key

# Ordenação por mistura
def merge_sort(arr, p=0, r=None):
    
    if r is None:
        r = len(arr)
        
    if(r - p > 1):
        q = (p + r)//2
        mergesort(arr, p, q)
        mergesort(arr, q, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    # Novos arranjos
    left = arr[p:q]
    right = arr[q:r]
    top_left, top_right = 0, 0
    
    for k in range(p, r):
        if top_left >= len(left):
            arr[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            arr[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            arr[k] = left[top_left]
            top_left = top_left + 1
        else:
            arr[k] = right[top_right]
            top_right = top_right + 1
            
# Inverter listas
def reverse_list(arr):
    size = len(arr)
    limit = size//2
    for i in range(limit):
        aux = arr[i]
        arr[i] = arr[size-i-1]
        arr[size-i-1] = aux

# 4 + N complexidade de tamanho
# 2 + 4*(N/2) == 2 + 2*N complexidade de tempo = O(N)


# Procura por elementos duplicados
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