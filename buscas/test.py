from busca import search

if __name__ == "__main__":
    # Teste de Busca
    strange_list = [8, "5", 32, 0, "python", 11]
    elem = 32
    
    index = search(strange_list, elem)
    if index is not None:
        print(f"O índice do elemento {elem} é {index}")
    else:
        print(f"O elemento {elem} não se encontra na lista.")