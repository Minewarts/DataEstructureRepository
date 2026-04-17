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
    self.size += 1

  def deQueue(self):
    if self.head is None:
      return None
    nodo = self.head
    self.head = nodo.next
    if self.head is None:
      self.tail = None
    self.size -= 1
    return nodo.dato
  
  def is_empty(self):
    return self.size == 0
  
  def generate(self, n, min_val=1, max_val=100):
    import random
    for _ in range(n):
      self.inQueue(random.randint(min_val, max_val))
  

  def __str__(self):
    result = []
    current = self.head
    while current is not None:
      result.append(str(current.dato))
      current = current.next
    return ' -- '.join(result)


class Stack:

  def __init__(self):
    self.top = None
    self.size = 0

  def push(self, elemento):
    nodo = QueueNode(elemento)
    nodo.next = self.top
    self.top = nodo
    self.size += 1

  def pop(self):
    if self.top is None:
      return None
    nodo = self.top
    self.top = nodo.next
    self.size -= 1
    return nodo.dato
  
  def __str__(self):
    result = []
    current = self.top
    while current is not None:
      result.append(str(current.dato))
      current = current.next
    return ' | '.join(result)

  def is_empty(self):
    return self.size == 0
  
  def generate_random_stack(self, n):
    import random
    for _ in range(n):
      self.push(random.randint(1, 100))
