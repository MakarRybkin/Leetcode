"""
AVL дерево - BST, которое балансирует дерево, не давая
дереву становиться бамбуком, переподвешивая концы дерева.

Есть 4 вида переподвешивания LL,RR,LR,RL
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # ---------- Вспомогательные методы ----------
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Поворот
        x.right = y
        y.left = T2

        # Обновление высот
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Поворот
        y.left = x
        x.right = T2

        # Обновление высот
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # ---------- Вставка ----------
    def insert(self, root, key):
        # 1. Обычная вставка в BST
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Обновляем высоту узла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Проверяем баланс
        balance = self.get_balance(root)

        # 4. Балансируем (4 случая)
        if balance > 1 and key < root.left.key:      # Left Left
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:    # Right Right
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:      # Left Right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:    # Right Left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ---------- Нахождение минимального узла ----------
    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # ---------- Удаление ----------
    def delete(self, root, key):
        # 1. Обычное удаление BST
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Узел найден
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Два потомка — берём inorder successor (минимальный справа)
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # 2. Обновление высоты
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Проверка баланса
        balance = self.get_balance(root)

        # 4. Балансировка
        if balance > 1 and self.get_balance(root.left) >= 0:  # Left Left
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:   # Left Right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:  # Right Right
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:   # Right Left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ---------- Обход ----------
    def pre_order(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)


tree = AVLTree()
root = None

# Вставка
nums = [10, 20, 30, 40, 50, 25]
for num in nums:
    root = tree.insert(root, num)

print("Префиксный обход (до удаления):")
tree.pre_order(root)
print("\n")
# The constructed AVL Tree would be
#        30
#       /  \
#      20   40
#     /  \    \
#    10  25   50
# Удаление узлов
root = tree.delete(root, 40)
print("После удаления 40:")
tree.pre_order(root)

