class BinaryTreeNode:

  def __init__(self, data):
    self.data = data
    self.leftchild = None
    self.rightchild = None


  def __str__(self, level=0):
    ret = "  " *level + str(self.data) + "\n"
    if self.leftchild:
       ret += self.leftchild.__str__(level+1)
    if self.rightchild:
       ret += self.rightchild.__str__(level+1)
    return ret


def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)

def in_order(root):

  if root is None:
    return

  in_order(root.leftchild)
  print(root.data)
  in_order(root.rightchild)


def reverse_in_order(root):

  if root is None:
    return

  reverse_in_order(root.rightchild)
  print(root.data)
  reverse_in_order(root.leftchild)


#Clase base  Cola
import random

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

  def pop(self):

    if self.__head is None:
      print("No hay elementos en la lista")
      return None
    elif self.__size == 1:
      popped_node = self.__head
      self.__head = None
      self.__tail = None
      self.__size = 0
      return popped_node
    else:
      #print("self.__tail",self.__tail)
      popped_node = self.__tail
      #obtener el penultimo
      #1ra forma new_tail = self.get_by_index(customll.size-2)

      #2da forma
      current_node = self.__head
      for _ in range(self.__size-2):
        current_node = current_node.next
      current_node.next = None
      self.__tail = current_node
      self.__size -= 1
      return popped_node



class Queue:

  def __init__(self):
    self.__q = LinkedList()


  def enqueue(self, e):
    self.__q.append(e)
    return True

  def dequeue(self):

    if self.is_empty():
      return "No hay elementos en la cola"

    temp_node = self.__q.popfirst()
    return temp_node.value

  def is_empty(self):

    return self.__q.size == 0

  def len(self):
    return self.__q.size

  def firs(self):
    if self.is_empty():
      return "No hay elementos en la cola"

    return self.__queue.head.value


  def __str__(self):
    result = [str(nodo.value) for nodo in self.__q]
    return ' -- '.join(result)

def level_order(root):
  if root is None:
    return

  aux_queue = Queue()
  aux_queue.enqueue(root)

  while not aux_queue.is_empty():
    #print("cola antes de iniciar el ciclo : ", aux_queue)
    cur_root = aux_queue.dequeue()

    print(cur_root.data)

    if cur_root.leftchild:
      aux_queue.enqueue(cur_root.leftchild)

    if cur_root.rightchild:
      aux_queue.enqueue(cur_root.rightchild)

def insert_node_bst(root, newdata):
  if root is None:
    return BinaryTreeNode(newdata)

  if newdata.id < root.data.id:
    root.leftchild = insert_node_bst(root.leftchild, newdata)
  else:
    root.rightchild = insert_node_bst(root.rightchild, newdata)

  return root

def search_node_bst(root, value_to_find):

  if root is None:
    return "El valor {} NO fue encontrado ó arbol vacio".format(value_to_find)

  print("Recorrido del arbol : ", root.data)
  if value_to_find == root.data:
    return "El valor {} SI fue encontrado".format(value_to_find)
  elif value_to_find < root.data:
    return search_node_bst(root.leftchild, value_to_find)
  else:
    return search_node_bst(root.rightchild, value_to_find)
  

def min_sucessor(root):

  if root.leftchild:
    return min_sucessor(root.leftchild)
  print("min Sucesor : ", root.data)
  return root

def max_sucessor(root):

  if root.rightchild:
    return max_sucessor(root.rightchild)

  print("max Sucesor : ", root.data)
  return root


def delete_node_bst(root, value_to_delete):
  if root is None:
    return None

  if value_to_delete < root.data.id:
    root.leftchild = delete_node_bst(root.leftchild, value_to_delete)
  elif value_to_delete > root.data.id:
    root.rightchild = delete_node_bst(root.rightchild, value_to_delete)
  else:
    if root.leftchild is None and root.rightchild is None:
      return None
    elif root.leftchild and root.rightchild:
      sucessor = min_sucessor(root.rightchild)
      temp_value = sucessor.data
      root.rightchild = delete_node_bst(root.rightchild, temp_value.id)
      root.data = temp_value
    elif root.leftchild:
      return root.leftchild
    else:
      return root.rightchild

  return root
