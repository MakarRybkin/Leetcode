from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=''.join(str(x) for x in digits)
        result=[int(x) for x in str(int(number)+1)]
        return result
print(Solution().plusOne([1,2,9]))