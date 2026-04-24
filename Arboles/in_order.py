import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from binary_tree import BinaryTreeNode, printTree, root_bt

def in_order(root):

  if root is None:
    return


  in_order(root.leftchild)
  print(root.data)
  in_order(root.rightchild)


'''printTree(root_bt)
print("\n")
in_order(root_bt)'''