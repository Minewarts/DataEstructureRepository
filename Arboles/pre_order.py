import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from binary_tree import BinaryTreeNode, printTree, root_bt

def pre_order(root):

  if root is None:
    return

  print(root.data)
  pre_order(root.leftchild)
  pre_order(root.rightchild)

'''
printTree(root_bt)
print("\n")
pre_order(root_bt)'''