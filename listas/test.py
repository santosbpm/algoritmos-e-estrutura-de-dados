from listas import Node

# teste do nó
if __name__ == "__main__":
    no1 = Node(5)
    no2 = Node(9)
    print(no1.data)
    print(no2.data)
    no1.next = no2
    print(no1.next)