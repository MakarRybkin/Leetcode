import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.probabilities = [self.weights[i] / sum(self.weights) for i in range(len(self.weights))]
    def pickIndex(self) -> int:
        return random.choices(range(len(self.weights)), weights=self.probabilities)[0]

obj = Solution([1,3])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())

