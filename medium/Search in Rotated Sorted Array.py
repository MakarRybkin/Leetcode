from typing import List


class Solution:
    def binary_search(self,sorted_nums,target,nums):
        start,finish = 0, len(sorted_nums) - 1
        while start<=finish:
            mid = (start+finish)//2
            if sorted_nums[mid]==target:
                return nums.index(target)
            elif sorted_nums[mid] > target:
                finish = mid - 1
            elif sorted_nums[mid] < target:
                start = mid + 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        start = nums[0]
        sorted_nums=[]
        if len(nums)==1:
            if nums[0] == target:
                return 0
            else:
                return -1
        for i in range(len(nums)) :
            if nums[i]<start:
                sorted_nums = nums[i:len(nums)] + nums[:i]
                break
            if i == len(nums)-1:
                sorted_nums = nums
        return self.binary_search(sorted_nums, target,nums)
print(Solution().search([1,3], 4))

