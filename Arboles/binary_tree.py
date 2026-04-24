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


'''print(root_bt)
print("\n")

#print(left_bt)


printTree(root_bt)'''
