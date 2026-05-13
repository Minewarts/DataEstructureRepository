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

tree = BinaryTreeNode(1)
tree.autogenerate(20)

def invert_binary_tree(root):
    if root is None:
        return None

    root.leftchild, root.rightchild = root.rightchild, root.leftchild
    invert_binary_tree(root.leftchild)
    invert_binary_tree(root.rightchild)
    return root

def search_leaves_r(root, value_to_count):
    if root is None:
        return 0

    if root.leftchild is None and root.rightchild is None:
        if root.data == value_to_count:
            return 1
        else:
            return 0

    return search_leaves_r(root.leftchild, value_to_count) + search_leaves_r(root.rightchild, value_to_count)


printTree(tree)

def first_common_ancestor(root, node1, node2):
    if root is None:
        return None

    if root.data == node1 or root.data == node2:
        return root

    left_lca = first_common_ancestor(root.leftchild, node1, node2)
    right_lca = first_common_ancestor(root.rightchild, node1, node2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca