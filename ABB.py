class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self):
        if self is not None:
            print self.value
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()
            print self.value
        
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print self.value
            if self.right is not None:
                self.right.inorder()

    def remove(self,value):
        if self is None:
            return
        if value < self.value:
            self.left = self.left.remove(value)
        elif value > self.value:
            self.right = self.right.remove(value)
        else: # got cha!
            # case 1: no childs
            if self.left is None and self.right is None:
                self = None
            # case 2: 1 child
            # left child null
            elif self.left is None:
                aux = self
                self = self.right
                aux = None # free
            # right child null
            elif self.right is None:
                aux = self
                self = self.left
                aux = None # free
            # case 3: 2 childs
            else:
                aux = self.right.findMin()
                self.value = aux.value
                self.right = self.right.remove(aux.value)
        return self

    def findMin(self):
        while self.left is not None:
            self = self.left
        return self

    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(),self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        # only root
        else:
            return 1

class ABB:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def height(self):
        if not self.isEmpty():
            return self.root.height()
        else:
            return 0

    # def height(self,aux_node):
    #     if aux_node == None:
    #         return 0
    #     return max(1+self.height(aux_node.left),1+self.height(aux_node.right))
        
    def insert(self, new_node):
        if self.isEmpty():
            self.root = new_node
        else:
            aux = self.root
            while aux:
                if new_node.value < aux.value:
                    if aux.left is None: 
                        aux.left = new_node
                        return
                    aux = aux.left
                elif new_node.value > aux.value:
                    if aux.right is None:
                        aux.right = new_node
                        return 
                    aux = aux.right

    def remove(self,value):
        print "Borrando",value
        self.root.remove(value)

    def preorder(self):
        print "Preorder"
        self.root.preorder()

    def postorder(self):
        print "Postorder"
        self.root.postorder()
    
    def inorder(self):
        print "Inorder"
        self.root.inorder()

if __name__ == "__main__":
    tree = ABB()

    h1 = Node(50)
    h2 = Node(25)
    h3 = Node(75)
    h4 = Node(10)
    h5 = Node(40)
    h6 = Node(60)
    h7 = Node(90)
    h8 = Node(35)
    h9 = Node(45)
    h10 = Node(70)
    h11 = Node(42)

    tree.insert(h1)
    tree.insert(h2)
    tree.insert(h3)
    tree.insert(h4)
    tree.insert(h5)
    tree.insert(h6)
    tree.insert(h7)
    tree.insert(h8)
    tree.insert(h9)
    tree.insert(h10)
    tree.insert(h11)

    tree.preorder()
    # print "Altura:",tree.height(tree.root)
    print "Altura:",tree.height()

    tree.remove(42)

    # tree.preorder()
    # print "Altura",tree.height(tree.root)
    print "Altura:",tree.height()