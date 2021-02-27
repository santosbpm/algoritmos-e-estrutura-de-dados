''' 
    Código de teste retirado do canal Programação Dinâmico (Python Café)
    GitHub do código: https://github.com/python-cafe/algorithms.git
'''
import random
from algorithms import insertion_sort, merge_sort, reverse_list, duplicate_elements, search


any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 
                    32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]

strange_list = [8, "5", 32, 0, "python", 11]

if __name__ == "__main__":
    # Teste para ordenção de lista
    """ test_cases = {'Números aleatórios': any_numbers, 
                    'Já ordenados': already_sorted, 
                    'Ordem inversa': inversed, 
                    'Elementos repetidos': repeated
                }
    print("*******************************")
    for name, arr in test_cases.items():
        print(f"\nCaso de teste: {name}")
        print(arr)
        reverse_list(arr)
        print("\n Ordenado:")
        print(arr)
    print("*******************************") """
    
    
    # Teste de Busca
    elem = 32
    index = search(strange_list, elem)
    if index is not None:
        print(f"O índice do elemento {elem} é {index}")
    else:
        print(f"O elemento {elem} não se encontra na lista.")