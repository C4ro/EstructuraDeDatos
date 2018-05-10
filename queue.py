import stack

class Node:
    def __init__(self,x):
        self.x = x
        self. next = None

class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def push(self, new_node):
        if self.is_empty():
            self.head = new_node
        else:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = new_node

    def pop(self):
        aux = self.head
        self.head = self.head.next
        aux.next = None
        return aux

    def front(self):
        if not self.is_empty():
            return self.head
        
    def back(self):
        if not self.is_empty():
            aux = self.head
            while aux.next:
                aux = aux.next
            return aux

    def printQueue(self):
        if not self.is_empty():
            aux = self.head
            while aux:
                print aux.x
                aux = aux.next

    def invert(self):
        if not self.is_empty():
            aux_stack = stack.Stack()
            while not self.is_empty():
                aux_stack.push(self.pop())
            while not aux_stack.empty():
                self.push(aux_stack.pop())
        return self                          
        
if __name__ == "__main__":
    queue = Queue()
    node1 = Node(5)
    node2 = Node(7)
    node3 = Node(2)
    node4 = Node(3)
    queue.push(node1)
    queue.push(node2)
    queue.push(node3)
    queue.push(node4)
    print "cola:"
    queue.printQueue()
    print "\ncola invertida:\n"
    queue.invert()
    queue.printQueue()
    