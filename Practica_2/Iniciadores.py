import random
class Vehiculo:
  __slots__ = ('placa', 'tipo', 'prioridad', 'revisado', 'next', 'prev')

  def priority_validation(self):
    if self.__prio < 0 or self.__prio > 5:
      raise ValueError("La prioridad debe ser un numero entre 0 y 5")

  def __init__(self, placa: str, tipo: str, prioridad: int) -> None:
    self.placa = placa
    self.tipo = tipo
    self.prioridad = prioridad
    self.revisado = False
    self.next = None
    self.prev = None

  
  def __str__(self):
    return self.placa

  @property
  def type(self):
    return self.tipo


  @property
  def value(self):
    return self.placa

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.placa = newValue


class Via:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,Vehiculo):
      raise TypeError("head debe ser un objeto Vehiculo o None")
    self.__head = node

  @property
  def tail(self):
    return self.__tail

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,Vehiculo):
      raise TypeError("tail debe ser un objeto Vehiculo o None")
    self.__tail = node

  @property
  def size(self):
    return self.__size

  @size.setter
  def size(self,new_size):
    if not isinstance(new_size,int):
      raise TypeError("size debe ser un numero entero")
    self.__size = new_size

  def __str__(self):
    if self.__head is None:
      return 'Vía vacía'
    return ' <--> '.join(str(nodo) for nodo in self)

  def print(self):
    for nodo in self:
      print(str(nodo))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, vehiculo):
    if not isinstance(vehiculo, Vehiculo):
      raise TypeError('Solo se pueden prependear Vehiculo')

    vehiculo.next = self.__head
    vehiculo.prev = None

    if self.__head is not None:
      self.__head.prev = vehiculo
    else:
      self.__tail = vehiculo

    self.__head = vehiculo
    self.__size += 1

  def append(self, vehiculo):
    if not isinstance(vehiculo, Vehiculo):
      raise TypeError('Solo se pueden appendear Vehiculo')

    vehiculo.prev = self.__tail
    vehiculo.next = None

    if self.__tail is not None:
      self.__tail.next = vehiculo
    else:
      self.__head = vehiculo

    self.__tail = vehiculo
    self.__size += 1

  def getbyindex(self, index):
    if index < 0 or index > self.__size:
      return "Error, indice fuera de rango"

    cont = 0
    for currentNode in self:
      if cont == index:
        return currentNode
      cont += 1

  def insertinindex(self, value, index):

    if not isinstance(value, Vehiculo):
      raise TypeError('Solo se pueden insertar objetos Vehiculo')

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      nextNode = prevNode.next
      newNode = value
      newNode.next = nextNode
      newNode.prev = prevNode
      prevNode.next = newNode
      if nextNode is not None:
        nextNode.prev = newNode
      self.__size += 1

  def searchbyvalue(self, valuetosearch):
    for currentNode in self:
      if currentNode.value == valuetosearch:
        return True

    return False

  def setnewvalue(self, valuetochange, newvalue):
    for currentNode in self:
      if currentNode.value == valuetochange:
        currentNode.value = newvalue
        return True

    return False

  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__head.prev = None

      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode


  def pop(self):
    tempNode = self.__tail
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__tail = self.__tail.prev
      self.__tail.next = None

      self.__size -= 1

    tempNode.prev = None  #limpiar la referencia al penultimo nodo, ahora nueva cola
    return tempNode


  def generate(self, num, min, max):
    for _ in range(num):
      self.append(random.randint(min,max))


class Node:
  __slots__ = ('__value','__next')

  def __init__(self,value):
    self.__value = value
    self.__next = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class LinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = node

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = node

  @size.setter
  def size(self,num):
    self.__size = num

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def append(self,value): # Adicionar al final
    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      self.__tail = newnode
    self.__size += 1


  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return False
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode



class ColaNodo:
  __slots__ = ('dato','next')

  def __init__(self, dato):
    self.dato = dato
    self.next = None


class Queue:

  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def encolar(self, elemento):
    nodo = ColaNodo(elemento)
    if self.tail is None:
      self.head = nodo
      self.tail = nodo
    else:
      self.tail.next = nodo
      self.tail = nodo
    self._size += 1

  def desencolar(self):
    if self.head is None:
      return None
    nodo = self.head
    self.head = nodo.next
    if self.head is None:
      self.tail = None
    self._size -= 1
    return nodo.dato

  def esta_vacia(self):
    return self._size == 0

  def tamano(self):
    return self._size

  # Aliases para compatibilidad con el código existente
  def enqueue(self, e):
    return self.encolar(e)

  def dequeue(self):
    return self.desencolar()

  def is_empty(self):
    return self.esta_vacia()

  def len(self):
    return self.tamano()

  def __str__(self):
    result = []
    current = self.head
    while current is not None:
      result.append(str(current.dato))
      current = current.next
    return ' -- '.join(result)

