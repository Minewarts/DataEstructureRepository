#CLASE BASE

import random

class NodeD:
  __slots__ = ('__value','__next','__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__prev = node


  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__head = node

  @property
  def tail(self):
    return self.__tail

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,NodeD):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
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

  def prepend(self, value):

    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head #enlazo nuevo nodo
      self.__head.prev = newnode
      self.__head = newnode
    self.__size += 1

  def append(self,value):
    newnode = NodeD(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      newnode.prev = self.__tail
      self.__tail = newnode

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

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      nextNode = prevNode.next
      newNode = NodeD(value)
      newNode.next = prevNode.next #Enlazo el next del nuevo nodo, que es el next del previo
      newNode.prev = prevNode # previo del nodo nuevo
      nextNode.prev = newNode # previo del nodo next antes de la inserción
      prevNode.next = newNode
      self.__size +=1

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