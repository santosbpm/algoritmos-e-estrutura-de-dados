from linkedlist import LinkedList

# teste do lista encadeada
if __name__ == "__main__":
    lista = LinkedList()
    lista.append(7)
    lista.append(80)
    lista.append(56)
    lista.append(32)
    lista.append(17)
    print(len(lista))
    print(lista[0])
    print(lista.index(7))
    lista.insert(0, 22)
    print(lista[0])