class Plato:
  def __init__(self, color, diametro):
    self.color = color
    self.diametro = diametro
    self.next = None

class PilaDePlatos:
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None
    
  def push(self,nuevo_plato):
    if self.is_empty():
        self.head = nuevo_plato
    else:
        nuevo_plato.next = self.head
        self.head = nuevo_plato

  def pop(self):
    if not self.is_empty():
        self.head = self.head.next

  def cantidad_por_color(self, color):
    if not self.is_empty():
        aux = self.head
        cont = 0
        while aux:
            if aux.color == color:
                cont += 1
        return cont
                
