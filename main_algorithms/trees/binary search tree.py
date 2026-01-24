"""
BST главное преимущество перед обычным binary search на массиве
это добавление/удаление элементов за O(logn), но требует чуть
больше памяти
"""

class Node:
    """Узел BST"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Бинарное дерево поиска (BST)"""
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value):
        """Удаление узла со значением value"""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Узел найден
            if node.left is None and node.right is None:
                return None  # Листовой узел
            elif node.left is None:
                return node.right  # Только правый ребёнок
            elif node.right is None:
                return node.left   # Только левый ребёнок
            else:
                # Два ребёнка: найти минимальный элемент в правом поддереве
                min_larger_node = self._find_min(node.right)
                node.value = min_larger_node.value
                node.right = self._delete_recursive(node.right, min_larger_node.value)
        return node

    def _find_min(self, node):
        """Находит минимальный элемент в поддереве"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Обходы дерева
    def inorder(self, node):
        result = []
        if node:
            result.extend(self.inorder(node.left))
            result.append(node.value)
            result.extend(self.inorder(node.right))
        return result

    def preorder(self, node):
        result = []
        if node:
            result.append(node.value)
            result.extend(self.preorder(node.left))
            result.extend(self.preorder(node.right))
        return result

    def postorder(self, node):
        result = []
        if node:
            result.extend(self.postorder(node.left))
            result.extend(self.postorder(node.right))
            result.append(node.value)
        return result



bst = BinarySearchTree()
for value in [7, 3, 9, 1, 5, 8, 10]:
    bst.insert(value)

print("Inorder:", bst.inorder(bst.root))    # [1, 3, 5, 7, 8, 9, 10] — отсортировано
print("Preorder:", bst.preorder(bst.root))  # [7, 3, 1, 5, 9, 8, 10]
print("Postorder:", bst.postorder(bst.root))# [1, 5, 3, 8, 10, 9, 7]

print("Поиск 5:", bst.search(5))  # True
print("Поиск 6:", bst.search(6))  # False

bst.delete(1)  # удалить лист
print("Удалили 1:", bst.inorder(bst.root))  # [3, 5, 7, 8, 9, 10]

bst.delete(9)  # удалить узел с двумя детьми
print("Удалили 9:", bst.inorder(bst.root))  # [3, 5, 7, 8, 10]

bst.delete(3)  # удалить узел с одним ребёнком
print("Удалили 3:", bst.inorder(bst.root))  # [5, 7, 8, 10]





"""
Проверить является ли binary tree binary search tree
"""


# Helper function to check if a tree is
# BST within a given range
def isBstUtil(node, min_val, max_val):
    if node is None:
        return True

    # If the current node's data
    # is not in the valid range, return false
    if node.value < min_val or node.value > max_val:
        return False

    # Recursively check the left and
    # right subtrees with updated ranges
    return (isBstUtil(node.left, min_val, node.value - 1) and
            isBstUtil(node.right, node.value + 1, max_val))


# Function to check if the entire binary tree is a BST
def isBST(root):
    return isBstUtil(root, float('-inf'), float('inf'))


if __name__ == "__main__":

    # Create a sample binary tree
    #     10
    #    /  \
    #   5    20
    #        / \
    #       9   25

    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.left = Node(9)
    root.right.right = Node(25)

    if isBST(root):
        print("true")
    else:
        print("false")
