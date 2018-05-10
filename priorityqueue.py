class Node:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority
        self.next = None

    def __str__(self):
        return ("{}({})".format(str(self.value), str(self.priority)))

class PriorityQueue:
    def __init__(self):
        self.head = None
    
    def empty(self):
        return self.head == None

    def push(self, new_node): # encolar por orden de prioridad
        if self.empty():
            self.head = new_node
        else:
            if new_node.priority > self.head.priority:
                new_node.next = self.head
                self.head = new_node
            else:
                prev_aux = self.head
                aux = self.head.next
                while aux:
                    if new_node.priority > aux.priority:
                        prev_aux.next = new_node
                        new_node.next = aux
                        return # = return None
                    prev_aux = aux
                    aux = aux.next
                prev_aux.next = new_node # en caso de que sea el de menor prioridad
                return
    
    def pop(self): # desencolar por orden de prioridad
        if not self.empty():
            aux = self.head
            self.head = self.head.next
            aux.next = None
            return aux
        print "Cola vacia"

    def printPQ(self):
        aux = self.head
        while aux:
            print "Valor:",aux.value,"Prioridad:",aux.priority
            aux = aux.next

if __name__ == "__main__":
    p = PriorityQueue()
    node1 = Node("a",7)
    node2 = Node("b",3)
    node3 = Node("c",9)
    node4 = Node("d",1)
    p.push(node1)
    p.push(node2)
    p.push(node3)
    p.push(node4)
    p.printPQ()
    p.pop()
    print "Sacando el de mayor prioridad...."
    p.printPQ()

    






            
                