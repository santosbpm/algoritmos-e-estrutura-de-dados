from node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self._size = 0 
    
    ''' Adiciona um elemento ao final da lista '''
    def append(self, elem):
        # Inserção quando a lista já possui elementos '''
        if self.head:
            pointer = self.head
            
            while pointer.next:
                pointer = pointer.next
            
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        
        self._size += 1
        
    ''' Retorna o tamanho da lista '''    
    def __len__(self):
        return self._size
    
    ''' Retorna o nó que se encontra no index indicada '''
    def _getnode(self, index):
        pointer = self.head
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer
    
    ''' Acessar determinado elemento da lista pelo índice '''
    def __getitem__(self, index):
        pointer = self._getnode(index)
        
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    ''' Modifica um valor que está em um determinado 
        lugar da lista '''
    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
        
    ''' Retorna o índice do elemento na lista '''
    def index(self, elem):
        pointer = self.head
        i = 0
        
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        
        raise ValueError(f"{elem} is not in list")
    
    ''' Insere um elemento em qualquer posição '''
    def insert(self, index, elem):
        node = Node(elem)
        
        if index == 0:
            
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1
        
    ''' Romove um elemento da lista '''
    def remove(self, elem):
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    # remove
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size -= 1
            return True
        raise ValueError(f"{elem} is not in list")