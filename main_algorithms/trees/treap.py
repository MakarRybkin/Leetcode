"""
Treap(tree + heap) - Декартово дерево или дерамида. В его нодах содержится
 (key, priority). Совмещает в себе BST,
значения которого являются ключами (key), и heap, значения которого
являются (priority).

Проще реализуется, чем Red-black tree и Avl, но нет гарантии высоты O(log(n)),
хотя в среднем O(log n). Позволяет решать больше задач чем RB и AVL
"""

import random

class Node:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(0, 100)  # случайный приоритет
        self.left = None
        self.right = None
        self.size = 1  # количество элементов в поддереве

    def __repr__(self):
        return f"({self.key}, pr={self.priority})"


def size(node):
    """Возвращает количество элементов в поддереве"""
    if node is None:
        return 0
    return node.size

def recalc(node):
    """Пересчитывает размер поддерева"""
    if node is not None:
        node.size = 1 + size(node.left) + size(node.right)



def split(root, key):
    """
    Разделяет дерево на два:
    L — все ключи < key
    R — все ключи >= key
    Возвращает (L, R)
    """
    if root is None:
        return (None, None)

    if root.key < key:
        # Корень должен попасть в левое поддерево
        left_sub, right_sub = split(root.right, key)
        root.right = left_sub
        recalc(root)
        return (root, right_sub)
    else:
        # Корень должен попасть в правое поддерево
        left_sub, right_sub = split(root.left, key)
        root.left = right_sub
        recalc(root)
        return (left_sub, root)



def merge(left, right):
    """
    Объединяет два дерева left и right в одно.
    Требование: все ключи в left < все ключи в right.
    """
    if left is None:
        return right
    if right is None:
        return left

    if left.priority > right.priority:
        left.right = merge(left.right, right)
        recalc(left)
        return left
    else:
        right.left = merge(left, right.left)
        recalc(right)
        return right


def insert(root, key):
    """
    Вставляет ключ key в дерево root.
    Возвращает новый корень.
    """
    new_node = Node(key)
    # Разделяем дерево на элементы меньше key и больше/равные key
    left, right = split(root, key)
    # Склеиваем: left + new_node + right
    root = merge(merge(left, new_node), right)
    return root


def erase(root, key):
    """
    Удаляет элемент с данным ключом из дерева.
    """
    if root is None:
        return None
    # Разделяем на три части: <key, ==key, >key
    left, mid = split(root, key)
    mid, right = split(mid, key + 1)
    # mid содержит удаляемый элемент, мы его просто выкидываем
    root = merge(left, right)
    return root



def inorder(root):
    """Возвращает список всех ключей по возрастанию"""
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)

def check_treap(node):
    """Проверяет, что дерево удовлетворяет свойствам BST и heap."""
    if node is None:
        return True, float('inf'), float('-inf')  # min, max пустого дерева

    # Проверяем поддеревья
    ok_left, min_left, max_left = check_treap(node.left)
    ok_right, min_right, max_right = check_treap(node.right)

    # Проверка BST-условия:
    # все ключи в левом поддереве < node.key < все ключи в правом поддереве
    bst_ok = (max_left < node.key < min_right)

    # Проверка heap-условия:
    # приоритет родителя больше, чем у потомков
    heap_ok = True
    if node.left and node.priority <= node.left.priority:
        heap_ok = False
    if node.right and node.priority <= node.right.priority:
        heap_ok = False

    # Вычисляем новый min/max
    min_val = min(min_left, node.key)
    max_val = max(max_right, node.key)

    ok = ok_left and ok_right and bst_ok and heap_ok
    return ok, min_val, max_val


random.seed(0)

root = None
for x in [5, 2, 8, 6, 3, 1, 7]:
    root = insert(root, x)
    print(f"После вставки {x}: {inorder(root)}")

ok, _, _ = check_treap(root)
print("После вставок корректен:", ok)

print("\nУдалим 5:")
root = erase(root, 5)
print("Результат:", inorder(root))

ok, _, _ = check_treap(root)
print("После вставок корректен:", ok)

print("\nРазделим по ключу 4:")
L, R = split(root, 4)
print("L =", inorder(L))
print("R =", inorder(R))

ok, _, _ = check_treap(L)
print("После вставок корректен:", ok)

print("\nСольём обратно:")
merged = merge(L, R)
print("Merged =", inorder(merged))

