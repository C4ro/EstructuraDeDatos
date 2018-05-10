import ordenamiento as order

class Node:
    def __init__(self, numero):
        self.numero = numero
        self.next = None
    def get_data(self):
        return numero

class Lista:
    def __init__(self):
        self.head = None
        self.size = 0

    # def ordenar(self):
    #     if self.vacio():
    #         print "Lista vacia"
    #     else:
    #         aux = self.head
    #         l = []
    #         while aux:
    #             l.append(aux)
    #             aux = aux.next
    #         l.sort(reverse=True)
    #         newlist = Lista()

    def insert_sort(self, numero):
        if self.vacio():
            self.head = Node(numero)
        else:
            actual = self.head
            nuevo = Node(numero)
            if actual.numero > nuevo.numero:
                nuevo.next = actual
                self.head = nuevo
            while actual.next:
                if actual.next.numero > nuevo.numero:
                    break
                actual = actual.next
            nuevo.next = actual.next
            actual.next = nuevo

    def select(self, i):
        aux = self.head
        count = 0
        while aux:
            if count == i:
                print "el elemento",i,"de la lista es: ", aux.numero
                return
            else:
                count = count + 1
                aux = aux.next
        print "elemento no esta en la lista"

    def posicion(self,x):
        aux = self.head
        pos = 0
        while aux:
            if aux.numero == x:
                print "la posicion del elemento",x,"en la lista es:",pos
                return 
            else:
                pos = pos + 1
                aux = aux.next
        print "elemento no esta en la lista"

    def pertenencia(self, numero):
        aux = self.head
        while aux:
            if aux.numero == numero:
                print "el numero", numero, "pertenece al conjunto"
                return
            aux = aux.next
        print "el numero", numero, "no esta en el conjunto"

    def vacio(self):
        if self.head == None:
            return True
        else:
            return False
    
    def minimo(self): # minimo esta al final siempre
        aux = self.head
        while aux:
            aux = aux.next
        return aux

    def insert_first(self, numero): # agrega al principio
        if self.vacio():
            self.head = Node(numero)
        else:
            node = Node(numero)
            node.next = self.head
            self.head = node
        
    def insert_last(self, numero):
        if self.vacio():
            self.head = Node(numero)
        else:
            aux = self.head
            while aux.next:
                aux = aux.next
            node = Node(numero)
            aux.next = node

    def print_list(self):
        if self.vacio(): 
            print "Lista vacia"
        else: 
            aux = self.head
            while aux:
                print "Numero: ", aux.numero
                aux = aux.next



if __name__ == "__main__":
    lista = Lista()
    lista.insert_sort(0)
    lista.insert_sort(400)
    lista.insert_sort(4)
    lista.insert_sort(5)
    lista.insert_sort(1)
    lista.insert_sort(20)
    # lista.pertenencia(20)
    # lista.pertenencia(1)
    # lista.pertenencia(8)
    # lista.posicion(20)
    lista.print_list()



        