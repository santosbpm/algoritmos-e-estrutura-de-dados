from linkedlist import LinkedList

# teste do lista encadeada
if __name__ == "__main__":
    lista = LinkedList()
    lista.append(7)
    lista.append(80)
    lista.append(56)
    print(len(lista))
    print(lista[2])
    print(lista.index(80))