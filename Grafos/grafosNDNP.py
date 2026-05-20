from Iniciadores import Queue, Stack


class Graph_DNP:
    """Grafo dirigido no ponderado."""

    def __init__(self):
        self.listadj = {}   # Lista de adyacencia

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.listadj:
            self.listadj[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.listadj:
            print(vertex, " : ", self.listadj[vertex])

    def vertices(self):
        return list(self.listadj.keys())

    def neighbors(self, vertex):
        if vertex not in self.listadj:
            raise ValueError("El vertice/nodo no existe")
        return list(self.listadj[vertex])

    def add_edge(self, vertex1, vertex2) -> bool:
        if vertex1 == vertex2:
            raise ValueError("No se puede crear una arista para el mismo vertice")
        if vertex1 not in self.listadj or vertex2 not in self.listadj:
            raise ValueError("Los vertices/nodos no existen")
        if vertex2 not in self.listadj[vertex1]:
            self.listadj[vertex1].append(vertex2)
            return True
        return False

    def remove_edge(self, vertex1, vertex2) -> bool:
        if vertex1 not in self.listadj or vertex2 not in self.listadj:
            raise ValueError("Los vertices/nodos no existen")
        if vertex2 in self.listadj[vertex1]:
            self.listadj[vertex1].remove(vertex2)
            return True
        return False

    def make_and_link(self, vertex_add, vertex_link) -> bool:
        self.add_vertex(vertex_add)
        self.add_vertex(vertex_link)
        return self.add_edge(vertex_add, vertex_link)

    def remove_vertex(self, vertex) -> bool:
        if vertex not in self.listadj:
            raise ValueError("El vertice/nodo no existe")
        del self.listadj[vertex]
        for v in self.listadj:
            if vertex in self.listadj[v]:
                self.listadj[v].remove(vertex)
        return True
    
    def recorrido_bfs(self, start_vertex):
        if start_vertex not in self.listadj:
            raise ValueError("El vertice/nodo no existe")

        aux_queue = Queue()
        visited = []
        aux_queue.enqueue(start_vertex)
        visited.append(start_vertex)

        while not aux_queue.is_empty():
            vertex = aux_queue.dequeue()
            for neighbor in self.listadj[vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    aux_queue.enqueue(neighbor)

        return visited

    def recorrido_dfs(self, start_vertex):
        if start_vertex not in self.listadj:
            raise ValueError("El vertice/nodo no existe")

        aux_stack = Stack()
        visited = []
        aux_stack.push(start_vertex)

        while not aux_stack.is_empty():
            vertex = aux_stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in self.listadj[vertex]:
                    if neighbor not in visited:
                        aux_stack.push(neighbor)

        return visited
    
    def recorrido_bfs(self, start_vertex, target_vertex):
        if start_vertex not in self.listadj:
            raise ValueError("El vertice/nodo no existe")

        aux_queue = Queue()
        visited = []
        aux_queue.enqueue(start_vertex)
        visited.append(start_vertex)

        while not aux_queue.is_empty():
            vertex = aux_queue.dequeue()
            for neighbor in self.listadj[vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    aux_queue.enqueue(neighbor)

                if neighbor == target_vertex:
                    return True
            

        return False


class Graph_NDNP(Graph_DNP):
    """Grafo no dirigido no ponderado."""

    def add_edge(self, vertex1, vertex2) -> bool:
        if vertex1 == vertex2:
            raise ValueError("No se puede crear una arista para el mismo vertice")
        if vertex1 not in self.listadj or vertex2 not in self.listadj:
            raise ValueError("Los vertices/nodos no existen")
        if vertex2 not in self.listadj[vertex1]:
            self.listadj[vertex1].append(vertex2)
            self.listadj[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2) -> bool:
        if vertex1 not in self.listadj or vertex2 not in self.listadj:
            raise ValueError("Los vertices/nodos no existen")
        removed = False
        if vertex2 in self.listadj[vertex1]:
            self.listadj[vertex1].remove(vertex2)
            removed = True
        if vertex1 in self.listadj[vertex2]:
            self.listadj[vertex2].remove(vertex1)
            removed = True
        return removed

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    for neighbor in graph.listadj[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

def count_routes(graph, start_vertex, target_vertex):
    aux_queue = Queue()
    count = 0
    aux_queue.enqueue((start_vertex, {start_vertex}))
    while not aux_queue.is_empty():
        current_vertex, path = aux_queue.dequeue()
        if current_vertex == target_vertex:
            count += 1
        for neighbor in graph.listadj[current_vertex]:
            if neighbor not in path:
                aux_queue.enqueue((neighbor, path | {neighbor}))
    return count


def has_cycle(graph):

    for vertex in graph.listadj:
        if helper_has_cycle(graph, vertex):
            print('El grafo es ciclico en el vertice: ', vertex)
            return True
        
    print(el gra) 