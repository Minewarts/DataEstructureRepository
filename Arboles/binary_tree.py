import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Pilas y colas'))
from Queue import Queue

import random

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
    
    def in_order(self):
        if self.leftchild:
            self.leftchild.in_order()
        print(self.data)
        if self.rightchild:
            self.rightchild.in_order()

    def pre_order(self):
        print(self.data)
        if self.leftchild:
            self.leftchild.pre_order()
        if self.rightchild:
            self.rightchild.pre_order()

    def post_order(self):
        if self.leftchild:
            self.leftchild.post_order()
        if self.rightchild:
            self.rightchild.post_order()
        print(self.data)

    def level_order(self):
        aux_queue = Queue()
        aux_queue.inQueue(self)

        while not aux_queue.is_empty():
            cur_root = aux_queue.deQueue()
            print(cur_root.data)
            if cur_root.leftchild:
                aux_queue.inQueue(cur_root.leftchild)
            if cur_root.rightchild:
                aux_queue.inQueue(cur_root.rightchild)

    def search_node(self, value_to_find):
        aux_queue = Queue()
        aux_queue.inQueue(self)

        while not aux_queue.is_empty():
            cur_root = aux_queue.deQueue()
            if cur_root.data == value_to_find:
                return cur_root
            print(cur_root.data)
            if cur_root.leftchild:
                aux_queue.inQueue(cur_root.leftchild)
            if cur_root.rightchild:
                aux_queue.inQueue(cur_root.rightchild)

        return "el valor {} NO fue encontrado".format(value_to_find)
    
    def insert_node_bt(self, newdata):
        aux_queue = Queue()
        aux_queue.inQueue(self)

        while not aux_queue.is_empty():
            cur_root = aux_queue.deQueue()
            if cur_root.leftchild is None:
                cur_root.leftchild = BinaryTreeNode(newdata)
                return self
            aux_queue.inQueue(cur_root.leftchild)
            if cur_root.rightchild is None:
                cur_root.rightchild = BinaryTreeNode(newdata)
                return self
            aux_queue.inQueue(cur_root.rightchild)

    def get_last_node(self):
        aux_queue = Queue()
        aux_queue.inQueue(self)

        last_node = None
        while not aux_queue.is_empty():
            last_node = aux_queue.deQueue()
            if last_node.leftchild:
                aux_queue.inQueue(last_node.leftchild)
            if last_node.rightchild:
                aux_queue.inQueue(last_node.rightchild)

        return last_node.data

    def delete_last_node(self):
        aux_queue = Queue()
        aux_queue.inQueue(self)

        parent = None
        last_node = None
        while not aux_queue.is_empty():
            last_node = aux_queue.deQueue()
            if last_node.leftchild:
                parent = last_node
                aux_queue.inQueue(last_node.leftchild)
            if last_node.rightchild:
                parent = last_node
                aux_queue.inQueue(last_node.rightchild)

        if parent is None:
            return None

        if parent.rightchild is last_node:
            parent.rightchild = None
        elif parent.leftchild is last_node:
            parent.leftchild = None

        return self

    def delete_node(self, value_to_delete):

        if self.leftchild is None and self.rightchild is None:
            if self.data == value_to_delete:
                return None
            return "el valor {} NO fue encontrado".format(value_to_delete)

        aux_queue = Queue()
        aux_queue.inQueue(self)

        while not aux_queue.is_empty():
            cur_root = aux_queue.deQueue()
            if cur_root.data == value_to_delete:
                last_node_value = self.get_last_node()
                cur_root.data = last_node_value
                self.delete_last_node()
                return self
            if cur_root.leftchild:
                aux_queue.inQueue(cur_root.leftchild)
            if cur_root.rightchild:
                aux_queue.inQueue(cur_root.rightchild)

        return "el valor {} NO fue encontrado".format(value_to_delete)


    def autogenerate(self, cuantity_nodes):
        while cuantity_nodes != 0:
            self.insert_node_bt(random.randint(1, 100))
            cuantity_nodes = cuantity_nodes - 1


        
    




def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)


root_bt = BinaryTreeNode("Libros")

left_bt = BinaryTreeNode("Suspenso")
rigth_bt = BinaryTreeNode("Fantasia")

root_bt.leftchild = left_bt
root_bt.rightchild = rigth_bt

left_bt.leftchild = BinaryTreeNode("Terror")
left_bt.rightchild = BinaryTreeNode("Crimenes")


rigth_bt.leftchild = BinaryTreeNode("Harry Potter")
rigth_bt.rightchild = BinaryTreeNode("El señor de los anillos")

left_bt.leftchild.leftchild = BinaryTreeNode("IT")
left_bt.leftchild.rightchild = BinaryTreeNode("El resplandor")

left_bt.rightchild.leftchild = BinaryTreeNode("Asesinatos 1")


"""print(root_bt)
print("\n")

#print(left_bt)


printTree(root_bt)"""
