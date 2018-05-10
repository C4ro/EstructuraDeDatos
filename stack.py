class Node:
    def __init__(self,x): # x: numero
        self.x=x
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

    def push(self,new_node):
        if self.empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        aux = self.head
        self.head = self.head.next
        aux.next = None
        return aux

    def top(self):
        return self.head
    
    def printStack(self):
        if not self.empty():
            aux = self.head
            while aux:
                print aux.x
                aux = aux.next

if __name__ == "__main__":
    stack = Stack()
    node1 = Node(5)
    node2 = Node(7)
    node3 = Node(2)
    node4 = Node(3)
    stack.push(node1)
    stack.push(node2)
    stack.push(node3)
    stack.push(node4)
    stack.pop()
    stack.printStack()

    


    
            


        


