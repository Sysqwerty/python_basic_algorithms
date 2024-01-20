class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(_root, _key):
    if not _root:
        return AVLNode(_key)

    if _key < _root.key:
        _root.left = insert(_root.left, _key)
    elif _key > _root.key:
        _root.right = insert(_root.right, _key)
    else:
        return _root

    _root.height = 1 + max(get_height(_root.left), get_height(_root.right))

    balance = get_balance(_root)

    if balance > 1:
        if _key < _root.left.key:
            return right_rotate(_root)
        else:
            _root.left = left_rotate(_root.left)
            return right_rotate(_root)

    if balance < -1:
        if _key > _root.right.key:
            return left_rotate(_root)
        else:
            _root.right = right_rotate(_root.right)
            return left_rotate(_root)

    return _root


def delete_node(_root, _key):
    if not _root:
        return _root

    if _key < _root.key:
        _root.left = delete_node(_root.left, _key)
    elif _key > _root.key:
        _root.right = delete_node(_root.right, _key)
    else:
        if _root.left is None:
            temp = _root.right
            _root = None
            return temp
        elif _root.right is None:
            temp = _root.left
            _root = None
            return temp

        temp = min_value_node(_root.right)
        _root.key = temp.key
        _root.right = delete_node(_root.right, temp.key)

    if _root is None:
        return _root

    _root.height = 1 + max(get_height(_root.left), get_height(_root.right))

    balance = get_balance(_root)

    if balance > 1:
        if get_balance(_root.left) >= 0:
            return right_rotate(_root)
        else:
            _root.left = left_rotate(_root.left)
            return right_rotate(_root)

    if balance < -1:
        if get_balance(_root.right) <= 0:
            return left_rotate(_root)
        else:
            _root.right = right_rotate(_root.right)
            return left_rotate(_root)

    return _root


# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)
    print("AVL-Дерево:")
    print(root)

# Delete
keys_to_delete = [10, 27]
for key in keys_to_delete:
    root = delete_node(root, key)
    print("Видалено:", key)
    print("AVL-Дерево:")
    print(root)
