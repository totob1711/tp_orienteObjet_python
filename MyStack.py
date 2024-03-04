class MyStack():
    
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = None
        self.size = 0
        
    def add_to_stack(self, object):
        self.object = object
        if self.is_full():
            raise MyOutOfSizeException("La pile est pleine")
        new_node = Node(object)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        
    def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException("La pile est vide")
        object = self.top.object
        self.top = self.top.next
        self.size -= 1
        return object
    
    def is_full(self):
        return self.size == self.max_size
    
    def is_empty(self):
        return self.size == 0 

class Node():
    
    def __init__(self, object):
        self.object = object
        self.next = None

class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass
        
if __name__ == '__main__':
    myStack = MyStack(input("Entrez la taille de la pile: "))
    myStack.add_to_stack('hello')
    myStack.add_to_stack('hello')
    print(myStack.is_full()) # False
    myStack.add_to_stack('hello')
    print(myStack.is_full()) # True
    try:
        myStack.add_to_stack('hello') # MyOutOfSizeException
    except MyOutOfSizeException:
        print("Erreur: La pile est pleine")
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # True
    try:
        print(myStack.pop_from_stack()) # MyEmptyStackException
    except MyEmptyStackException:
        print("Erreur: La pile est vide")