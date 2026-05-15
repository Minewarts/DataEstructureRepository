class Graph_DNP:
    def __init__(self):
        self.listadj = {}   #Lista de adjacencia

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.listadj:
            self.listadj[vertex] = [] 
            return True
        return False
    
    def print (self):
        for vertex in self.listadj:
            print(vertex, " : ", self.listadj[vertex])

    def add_edge(self, vertex1, vertex2) -> bool:
        if vertex1 == vertex2:
            ValueError("No se puede crear una arista para el mismo vertice")
        if vertex1 in self.listadj and vertex2 in self.listadj:
            if vertex2 not in self.listadj[vertex1]:
                self.listadj[vertex1].append(vertex2)
                return True
        else:
            ValueError("Los vertices / nodos no existen")
        return False

    def remove_edge(self, vertex1, vertex2) -> bool:
        if vertex1 in self.listadj and vertex2 in self.listadj:
            if vertex2 in self.listadj[vertex1]:
                self.listadj[vertex1].remove(vertex2)
                return True
        return False

    def make_and_link(self, vertex_add, vertex_link):
        if vertex_add not in self.listadj:
            self.add_vertex(vertex_add)
            self.add_edge(vertex_add, vertex_link)


    def remove_vertex(self, vertex):
        if vertex in self.listadj:
            del self.listadj[vertex]
            for v in self.listadj:
                if vertex in self.listadj[v]:
                    self.listadj[v].remove(vertex)

        raise ValueError("El vertice/nodo no existe")