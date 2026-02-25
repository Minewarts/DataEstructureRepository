'''Una lista enlazada es una estructura de datos lineal y dinámica compuesta por nodos no contiguos en memoria.
   Cada nodo contiene datos y un puntero (referencia) al siguiente nodo, permitiendo inserciones y eliminaciones 
   rápidas al actualizar los enlaces. Se accede secuencialmente empezando desde la cabeza (primer nodo).'''

''' add_first: Agrega un nuevo nodo al inicio de la lista.
    add_last: Agrega un nuevo nodo al final de la lista.
    remove_first: Elimina el primer nodo de la lista.
    remove_last: Elimina el último nodo de la lista.
    get_first: Devuelve el valor del primer nodo.
    get_last: Devuelve el valor del último nodo.
    is_empty: Verifica si la lista está vacía.
    size: Devuelve el número de nodos en la lista.'''


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

custom_list = LinkedList()
custom_list.prepend(10)
custom_list.append(40)
custom_list.append(50)
print("despues del primer append: ", custom_list)
print ("custom_list.head.data: ", custom_list.head.data)
print ("custom_list.tail.data: ", custom_list.tail.data)