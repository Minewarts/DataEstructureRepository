import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from level_order import level_order
from in_order import in_order
from pre_order import pre_order
from post_order import post_order
from binary_tree import BinaryTreeNode, printTree, root_bt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Pilas y colas'))
from Queue import Queue

# Busqueda

def search_node(root, value_to_find):

    if root is None:
        return "No hay elementos en el arbol"

    aux_queue = Queue()
    aux_queue.enqueue(root)

    while not aux_queue.is_empty():

        cur_root = aux_queue.dequeue()

        if cur_root.data == value_to_find:
            return "el valor {} fue encontrado".format(value_to_find)

        print(cur_root.data)
        if cur_root.leftchild:
            aux_queue.enqueue(cur_root.leftchild)

        if cur_root.rightchild:
            aux_queue.enqueue(cur_root.rightchild)

    return "el valor {} NO fue encontrado".format(value_to_find)


# Inserción

def insert_node_bt(root, newdata):

    if root is None:
        root = BinaryTreeNode(newdata)
        return root

    aux_queue = Queue()
    aux_queue.enqueue(root)

    while not aux_queue.is_empty():

        cur_root = aux_queue.dequeue()

        if cur_root.leftchild is None:
            cur_root.leftchild = BinaryTreeNode(newdata)
            return root
        aux_queue.enqueue(cur_root.leftchild)

        if cur_root.rightchild is None:
            cur_root.rightchild = BinaryTreeNode(newdata)
            return root
        aux_queue.enqueue(cur_root.rightchild)

