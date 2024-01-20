class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def postorder_traversal(_root):
    if _root:
        postorder_traversal(_root.left)
        postorder_traversal(_root.right)
        print(_root.val)


# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Зворотний обхід:")
postorder_traversal(root)
