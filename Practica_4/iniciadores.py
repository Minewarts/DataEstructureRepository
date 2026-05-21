class Queue:

  def __init__(self):
    self.__items = []


  def enqueue(self,e):
    self.__items.append(e)
    return True

  def dequeue(self):
    if self.is_empty():
      return "Error, no hay elementos para retornar"

    return self.__items.pop(0)

  def is_empty(self):
    return len(self.__items) == 0

  def len(self):
    return len(self.__items)

  def first(self):
     if self.is_empty():
      return "Error, no hay elementos para retornar"

     return self.__items[0]

  def __str__(self):
    return '--'.join(map(str,self.__items))


class Stack:

  def __init__(self):
    self.__items = []

  def push(self,e):
    self.__items.append(e)
    return True

  def pop(self):
    if self.is_empty():
      return "Error, no hay elementos para retornar"

    return self.__items.pop()

  def is_empty(self):
    return len(self.__items) == 0

  def len(self):
    return len(self.__items)

  def top(self):
     if self.is_empty():
      return "Error, no hay elementos para retornar"

     return self.__items[-1]

  def __str__(self):
    return '--'.join(map(str,reversed(self.__items)))



class Graph_NDNP:

  def __init__(self):
    self.listadj = {}

  @property
  def adjlist(self):
    return self.listadj

  def add_vertex(self, vertex):
    if vertex not in self.listadj:
      self.listadj[vertex] = []
      return True
    return False

  def print(self):

    for vertex in self.listadj:
      print(vertex, " : ", self.listadj[vertex])

  def add_edge(self, vertex1, vertex2):
    if vertex1 == vertex2:
      print("No se puede crear una arista para el mismo vertice")
      return False
    if vertex1 in self.listadj and vertex2 in self.listadj:

      if vertex2 not in self.listadj[vertex1]:
        self.listadj[vertex1].append(vertex2)

      if vertex1 not in self.listadj[vertex2]:
        self.listadj[vertex2].append(vertex1)

      return True

    raise ValueError("Los vertices/nodos no existen")



  def remove_edge(self, vertex1, vertex2):
    if vertex1 == vertex2:
      print("No se puede eliminar una arista para el mismo vertice")
      return False
    if vertex1 in self.listadj and vertex2 in self.listadj:

      if vertex2 in self.listadj[vertex1]:
        self.listadj[vertex1].remove(vertex2)

      if vertex1 in self.listadj[vertex2]:
        self.listadj[vertex2].remove(vertex1)

      return True

    raise ValueError("Los vertices/nodos no existen")

  def remove_vertex(self, vertex):

    if vertex in self.listadj:
      del self.listadj[vertex]

      for adjvertex in self.listadj.values():
        if vertex in adjvertex:
          adjvertex.remove(vertex)

      return True


    raise ValueError("El vertice/nodo no existe.")


class Graph_DNP:

  def __init__(self):
    self.listadj = {}

  @property
  def adjlist(self):
    return self.listadj

  def add_vertex(self, vertex):
    if vertex not in self.listadj:
      self.listadj[vertex] = []
      return True
    return False

  def print(self):

    for vertex in self.listadj:
      print(vertex, " : ", self.listadj[vertex])

  def add_edge(self, source_vertex, target_vertex):
    if source_vertex == target_vertex:
      print("No se puede crear una arista para el mismo vertice")
      return False
    if source_vertex in self.listadj and target_vertex in self.listadj:

      if target_vertex not in self.listadj[source_vertex]:
        self.listadj[source_vertex].append(target_vertex)

      return True

    raise ValueError("Los vertices/nodos no existen")



  def remove_edge(self, source_vertex, target_vertex):
    if source_vertex == target_vertex:
      print("No se puede eliminar una arista para el mismo vertice")
      return False
    if source_vertex in self.listadj and target_vertex in self.listadj:

      if target_vertex in self.listadj[source_vertex]:
        self.listadj[source_vertex].remove(target_vertex)


      return True

    raise ValueError("Los vertices/nodos no existen")

  def remove_vertex(self, vertex):

    if vertex in self.listadj:
      del self.listadj[vertex]

      for adjvertex in self.listadj.values():
        if vertex in adjvertex:
          adjvertex.remove(vertex)

      return True


    raise ValueError("El vertice/nodo no existe.")