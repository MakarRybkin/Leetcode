"""
Куча

Позволяет нам добавлять, удалять элементы
 и искать минмимум(max) за O(log n)

Обычно хранится как массив, дети хранятся по индексам
 левый - 2 * индекс предка и правый - 2 * индекс предка + 1
"""


class MinHeap:
    def __init__(self):
        self.heap = []  # внутреннее представление кучи в виде массива

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        """Поднимает элемент вверх, если нарушено свойство кучи"""
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    def _heapify_down(self, i):
        """Опускает элемент вниз, если нарушено свойство кучи"""
        smallest = i
        left = self._left(i)
        right = self._right(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def push(self, value):
        """Добавление элемента в кучу"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Удаляет и возвращает минимальный элемент"""
        if not self.heap:
            raise IndexError("pop from empty heap")

        min_value = self.heap[0]
        last_value = self.heap.pop()

        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)

        return min_value

    def peek(self):
        """Возвращает минимальный элемент без удаления"""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

h = MinHeap()
h.push(5)
h.push(3)
h.push(8)
h.push(1)

print("Куча:", h)        # Куча: [1, 3, 8, 5]
print("Минимум:", h.peek())  # Минимум: 1
print("Извлекаем:", h.pop()) # Извлекаем: 1
print("После удаления:", h)  # После удаления: [3, 5, 8]


"""
Можно реализовать с библиотекой heapq
"""

# A Python program to demonstrate common binary heap operations

# Import the heap functions from python library
from heapq import heappush, heappop, heapify


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

# A class for Min Heap
class MinHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)

        # Decrease value of key at index 'i' to new_val

    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)], self.heap[i])

    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]

heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.extractMin())
print(heapObj.getMin(),heapObj.decreaseKey(2, 1))
print(heapObj.getMin())
