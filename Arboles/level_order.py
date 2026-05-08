import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Pilas y colas'))

from binary_tree import BinaryTreeNode, printTree, root_bt
from Queue import Queue

def level_order(root):

  if root is None:
    return

  aux_queue = Queue()
  aux_queue.inQueue(root)

  while not aux_queue.is_empty():

    print("Estado de la cola al iniciar el ciclo :", aux_queue)
    cur_root = aux_queue.deQueue()

    print(cur_root.data)
    if cur_root.leftchild:
      aux_queue.inQueue(cur_root.leftchild)

    if cur_root.rightchild:
      aux_queue.inQueue(cur_root.rightchild)


'''printTree(root_bt)
print("\n")
level_order(root_bt)
level_order(root_bt)'''


