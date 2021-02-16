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