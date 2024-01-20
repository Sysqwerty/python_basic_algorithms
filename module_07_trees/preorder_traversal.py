class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def preorder_traversal(_root):
    if _root:
        print(_root.val)
        preorder_traversal(_root.left)
        preorder_traversal(_root.right)


# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Прямий обхід:")
preorder_traversal(root)
