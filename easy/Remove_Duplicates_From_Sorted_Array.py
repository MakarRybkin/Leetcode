from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        stop = len(nums)-1
        while i< stop:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                stop-=1
            else:
                i+=1
        return len(nums)
print(Solution().removeDuplicates([1,1,2,2,3,3]))