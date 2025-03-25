from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        l=0
        for r in range(len(nums)):
            if nums[r]!=val:
                nums[l]=nums[r]
                l+=1
            else:
                k+=1
        return len(nums)-k
print(Solution().removeElement([3,2,2,3,5,3], 3))