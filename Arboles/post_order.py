import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from binary_tree import BinaryTreeNode, printTree, root_bt

def post_order(root):

  if root is None:
    return


  post_order(root.leftchild)
  post_order(root.rightchild)
  print(root.data)


'''
printTree(root_bt)
print("\n")
post_order(root_bt)'''