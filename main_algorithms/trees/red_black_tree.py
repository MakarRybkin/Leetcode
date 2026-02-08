"""
Красно-черное дерево

Не так хорошо балансирует как AVL, но делает меньше переподвешиваний
при добавлении или удалении, поэтому быстрее
"""


class Node:
    def __init__(self, key=None, color='BLACK', left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"Node({self.key}, {self.color})"


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color='BLACK')
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL
        self.root = self.NIL

    def left_rotate(self, x):
        # Поворот влево вокруг узла x
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        # Поворот вправо вокруг узла y
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        # Стандартная BST вставка, потом фиксация свойств RB-tree
        node = Node(key=key, color='RED', left=self.NIL, right=self.NIL, parent=self.NIL)
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # Новый узел красный — нужно восстановить свойства
        self.insert_fixup(node)

    def insert_fixup(self, z):
        # Восстановление свойств после вставки, см. алгоритм CLRS
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # дядя
                if y.color == 'RED':
                    # случай 1: дядя красный
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # случай 2: превращаем в случай 3
                        z = z.parent
                        self.left_rotate(z)
                    # случай 3:
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:
                # зеркальное отражение
                y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'BLACK'

    def search(self, key):
        x = self.root
        while x != self.NIL and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x  # вернёт NIL, если не найдено

    def transplant(self, u, v):
        # Заменяет поддерево с корнем u на поддерево с корнем v
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def delete(self, key):
        z = self.search(key)
        if z == self.NIL:
            # Ничего нет для удаления
            return False
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self.delete_fixup(x)
        return True

    def delete_fixup(self, x):
        # Восстановление свойств после удаления (см. CLRS)
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    # случай 1
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    # случай 2
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.right.color == 'BLACK':
                        # случай 3
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.parent.right
                    # случай 4
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                # зеркальное отражение
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    # ---- Обходы и утилиты ----
    def inorder(self):
        # Возвращает список ключей в порядке возрастания
        res = []
        def _inorder(x):
            if x != self.NIL:
                _inorder(x.left)
                res.append((x.key, x.color))
                _inorder(x.right)
        _inorder(self.root)
        return res

    def pretty_print(self):
        # Печать дерева в текстовом виде (уровневый обход)
        if self.root == self.NIL:
            print("<пустое дерево>")
            return
        from collections import deque
        q = deque()
        q.append((self.root, 0))
        current_level = 0
        line = []
        while q:
            node, lvl = q.popleft()
            if lvl != current_level:
                print('  '.join(line))
                line = []
                current_level = lvl
            if node == self.NIL:
                line.append('NIL')
            else:
                line.append(f"{node.key}({node.color[0]})")
                q.append((node.left, lvl+1))
                q.append((node.right, lvl+1))
        if line:
            print('  '.join(line))

    def validate(self):
        # Проверяет все свойства красно-чёрного дерева:
        # 1) Корень чёрный
        # 2) NIL-узлы чёрные (в нашем случае всегда)
        # 3) Красный узел имеет чёрных детей
        # 4) Для каждого узла все пути до NIL содержат одинаковое число чёрных узлов

        if self.root.color != 'BLACK':
            return False, 'root is not black'

        def check_node(x):
            # возвращает (is_valid, black_height) для поддерева x
            if x == self.NIL:
                return True, 1  # считаем NIL как чёрный узел с черной высотой 1
            # правило: если узел красный, то оба ребёнка должны быть чёрными
            if x.color == 'RED':
                if x.left.color != 'BLACK' or x.right.color != 'BLACK':
                    return False, 0
            left_valid, left_bh = check_node(x.left)
            if not left_valid:
                return False, 0
            right_valid, right_bh = check_node(x.right)
            if not right_valid:
                return False, 0
            if left_bh != right_bh:
                return False, 0
            # черная высота: если текущий узел чёрный, прибавляем 1
            bh = left_bh + (1 if x.color == 'BLACK' else 0)
            return True, bh

        valid, _ = check_node(self.root)
        return valid, None if valid else 'rb properties violated'



tree = RedBlackTree()
data = [20, 15, 25, 10, 18, 8, 12, 16, 19, 30, 28, 40]
for v in data:
    tree.insert(v)
print('In-order (key, color):', tree.inorder())
tree.pretty_print()
valid, reason = tree.validate()
print('Valid:', valid, 'Reason:', reason)

print('\nУдаление 15, 20, 30')
tree.delete(15)
tree.delete(20)
tree.delete(30)
tree.pretty_print()
print('In-order после удаления:', tree.inorder())
valid, reason = tree.validate()
print('Valid после удаления:', valid, 'Reason:', reason)
