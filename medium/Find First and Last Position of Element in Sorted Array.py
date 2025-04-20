from typing import List


class Solution:
    def binary_search(self, nums ,target ) :
        start,finish = 0, len(nums) -1
        while start <= finish :
            mid = (start+finish)//2
            if nums[mid] == target :
                l,r = mid,mid
                while l>start and nums[l-1]==target:
                    l = l-1
                while r<finish and nums[r+1]==target:
                    r = r+1
                return [l,r]
            elif nums[mid] < target :
                start = mid+1
            elif nums[mid] > target:
                finish = mid-1
        return [-1,-1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(nums,target)
print(Solution().searchRange([5,7,7,8,8,8,8,8,10], 8))