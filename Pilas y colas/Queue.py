import random

class QueueNode:
  __slots__ = ('dato','next')

  def __init__(self, dato):
    self.dato = dato
    self.next = None


class Queue:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def inQueue(self, elemento):
    nodo = QueueNode(elemento)
    if self.tail is None:
      self.head = nodo
      self.tail = nodo
    else:
      self.tail.next = nodo
      self.tail = nodo
    self._size += 1

  def deQueue(self):
    if self.head is None:
      return None
    nodo = self.head
    self.head = nodo.next
    if self.head is None:
      self.tail = None
    self._size -= 1
    return nodo.dato
  
  def generate(self, n, min_value=0, max_value=100):
    for _ in range(n):
      self.inQueue(random.randint(min_value, max_value))

  def __str__(self):
    result = []
    current = self.head
    while current is not None:
      result.append(str(current.dato))
      current = current.next
    return ' -- '.join(result)