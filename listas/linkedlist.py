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
    
    ''' Acessar determinado elemento da lista pelo índice '''
    def __getitem__(self, index):
        pointer = self.head
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    ''' Modifica um valor que está em um determinado 
        lugar da lista '''
    def __setitem__(self, index, elem):
        pointer = self.head
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
        
    ''' Retorna o índidce do elemento na lista '''
    def index(self, elem):
        pointer = self.head
        i = 0
        
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        
        raise ValueError(f"{elem} is not in list")