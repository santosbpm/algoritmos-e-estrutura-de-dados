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
def mergesort(arr, p=0, r=None):
    
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
            
            
def reverse_list(arr):
    size = len(arr)
    limit = size//2
    for i in range(limit):
        aux = arr[i]
        arr[i] = arr[size-i]
        arr[size-i] = aux

# 4 + N complexidade de tamanho
# 2 + 4*(N/2) == 2 + 2*N complexidade de tempo