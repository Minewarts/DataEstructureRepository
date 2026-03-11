'''Una lista enlazada es una estructura de datos lineal y dinámica compuesta por nodos no contiguos en memoria.
   Cada nodo contiene datos y un puntero (referencia) al siguiente nodo, permitiendo inserciones y eliminaciones 
   rápidas al actualizar los enlaces. Se accede secuencialmente empezando desde la cabeza (primer nodo).'''

''' 
  Funciones:
- prepend: Agrega un nuevo nodo al inicio de la lista.
- append: Agrega un nuevo nodo al final de la lista.
- get_by_index: Devuelve el nodo en la posición especificada.
- insert_at_index: Inserta un nuevo nodo en la posición especificada.
- search_value: Busca un valor específico en la lista y devuelve True si se encuentra, de lo contrario, devuelve False.
- remove_first: Elimina el primer nodo de la lista y devuelve el nodo eliminado.
- remove_last: Elimina el último nodo de la lista y devuelve el nodo eliminado.
- clear: Elimina todos los nodos de la lista, dejando la lista vacía.
- generate_random: Genera una lista enlazada con un número específico de nodos, cada uno con un valor aleatorio dentro de un rango dado.
- return_n_to_last: Devuelve el nodo que se encuentra n posiciones desde el final de la lista.
- reverse: Invierte el orden de los nodos en la lista enlazada cambiando el puntero de cada nodo.
'''


class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next, Node):
            raise TypeError("El siguiente Valor debe ser un objeto de tipo Node o None.")
        self.__next = new_next

    @data.setter
    def data(self, new_data):
        if new_data is None:
            raise TypeError("El valor de data debe ser un número o una cadena.")
        self.__data = new_data

class LinkedList:

    __slots__=['__head', '__size', '__tail']
    def __init__(self):
        self.__head=None
        self.__size=0
        self.__tail=None

    @property
    def head(self):
        return self.__head
    
    @property
    def size(self): 
        return self.__size
    
    @property
    def tail(self):
        return self.__tail
    
    @head.setter
    def head(self, new_head):
        if new_head is not None and not isinstance(new_head, Node):
            raise TypeError("El valor de head debe ser un objeto de tipo Node o None.")
        self.__head = new_head

    @tail.setter
    def tail(self, new_tail):
        if new_tail is not None and not isinstance(new_tail, Node):
            raise TypeError("El valor de tail debe ser un objeto de tipo Node o None.")
        self.__tail = new_tail

    def __iter__(self):
        current_node=self.__head
        while current_node is not None:
            yield current_node.data
            current_node=current_node.next

    def __str__(self):
        result = [str(node) for node in self]
        return " -> ".join(result)
    
    def prepend(self, new_data):
        new_node = Node(new_data)
        if self.__head is None: 
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next=self.__head
            self.__head = new_node
        self.__size += 1

    def append(self, new_data):
        new_node=Node(new_data)
        if self.__tail is None:
            self.__head=new_node
            self.__tail=new_node
        else:
            self.__tail.next=new_node
            self.__tail=new_node
        self.__size += 1

    def get_by_index(self, index):
        if index < -1 or index > self.__size - 1:
            raise ValueError("Índice fuera de rango.")
        
        if index == -1:
            return self.__tail
        
        current_index = 0
        current_node = self.__head

        while current_node is not None:
            if index == current_index:
                return current_node
            
            current_index += 1
            current_node = current_node.next

    def insert_at_index(self,index, new_data):
        if index < -1 or index > self.__size - 1:
            raise ValueError("Índice fuera de rango.")
        
        if index == 0:
            self.prepend(new_data)
            
        elif index == -1 or index == self.__size:
            self.append(new_data)

        else:
            new_node = Node(new_data)
            prev_node = self.get_by_index(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.__size += 1
        
    def search_value(self, value):
        for current_node in self:
            if current_node == value:
                return True
        return False

    #def set_new_value(self, new_data):

    def remove_first(self):
        if self.__head is None:
            print("La lista está vacía.")
            return None
        
        if self.__size == 1:
            removed_node = self.__head
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return removed_node
        
        else:
            removed_node = self.__head
            self.__head = self.__head.next
            self.__size -= 1
            removed_node.next = None
            return removed_node
        
    def remove_last(self):
        if self.head is None:
            print("La lista está vacía.")
            return None
        if self.__size == 1:
            removed_node = self.__head
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return removed_node
        else:
            removed_node = self.__tail
            current_node = self.__head
            while current_node.next is not removed_node:
                current_node = current_node.next
            current_node.next = None
            self.__tail = current_node
            self.__size -= 1
            return removed_node
        
    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def generate_random(self, size, min_value, max_value):
        import random
        for _ in range(size):
            random_value = random.randint(min_value, max_value)
            self.append(random_value)

    def return_n_to_last(self, n):
        if n < 1 or n > self.__size:
            raise ValueError("n debe ser un número positivo menor o igual al tamaño de la lista.")
        
        target_index = self.__size - n
        return self.get_by_index(target_index)
    
    def reverse(self):
        prev_node = None
        current_node = self.__head
        self.__tail = self.__head  # El nodo actual de la cabeza se convertirá en la nueva cola

        while current_node is not None:
            next_node = current_node.next  # Guardar el siguiente nodo
            current_node.next = prev_node  # Invertir el enlace

            #Siguientes pasos para avanzar en la lista

            prev_node = current_node       # Mover prev_node al nodo actual
            current_node = next_node       # Mover al siguiente nodo
        
        self.__head = prev_node  # El último nodo procesado será la nueva cabeza

    def organize_by_pair_or_odd_position(self):
        odd_node=self.__head
        even_node=self.__head.next

        while even_node is not None and even_node.next is not None:
            odd_node.next=even_node.next
            odd_node=odd_node.next
            even_node.next=odd_node.next
            even_node=even_node.next


        odd_node.next=self.__head.next
        even_node.next=None

custom_list = LinkedList()
custom_list.generate_random(5, 1, 10)
print(custom_list)
print(custom_list.organize_by_pair_or_odd_position())