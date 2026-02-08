from typing import List


class Solution:
    def binary_search(self,sorted_nums,target,nums):
        start,finish = 0,len(sorted_nums) - 1
        while start <= finish:
            mid = (start+finish)//2
            if sorted_nums[mid] == target:
                return True
            elif sorted_nums[mid] < target:
                start = mid+1
            elif sorted_nums[mid] > target:
                finish = mid-1
        return False
    def search(self, nums: List[int], target: int) -> bool:
        start = nums[0]
        sorted_nums = []
        for i in reversed(range(len(nums))):
            if nums[i] > start:
                sorted_nums = nums[min(i+1,len(nums)):len(nums)]+nums[:min(i+1,len(nums))]
                break
            elif i == 0:
                sorted_nums = nums
        print(sorted_nums)
        start = sorted_nums[0]
        for i in range(len(nums)):
            if sorted_nums[i]<start:
                sorted_nums = sorted_nums[i:len(sorted_nums)] + sorted_nums[:i]
                break
        print(sorted_nums)
        return self.binary_search(sorted_nums,target,nums)
print(Solution().search([2,5,6,0,0,1,2], 0))

