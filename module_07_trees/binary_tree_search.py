class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(_root, key):
    if _root is None:
        return Node(key)
    else:
        if key < _root.val:
            _root.left = insert(_root.left, key)
        else:
            _root.right = insert(_root.right, key)
    return _root


def search(_root, key):
    if _root is None or _root.val == key:
        return _root
    if key < _root.val:
        return search(_root.left, key)
    return search(_root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(_root, key):
    if not _root:
        return _root

    if key < _root.val:
        _root.left = delete(_root.left, key)
    elif key > _root.val:
        _root.right = delete(_root.right, key)
    else:
        if not _root.left:
            temp = _root.right
            _root = None
            return temp
        elif not _root.right:
            temp = _root.left
            _root = None
            return temp
        _root.val = min_value_node(_root.right).val
        _root.right = delete(_root.right, _root.val)
    return _root


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
print(root)
root = delete(root, 8)
print(root)

# Пошук значення
val = 4
result = search(root, val)
if result:
    print(f"У дереві знайдено значення {result.val}")
else:
    print(f"У дереві не знайдено значення {val}")
