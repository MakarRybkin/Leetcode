# from typing import List
#
#
# class Solution:
#     def isSubarraySum(self,count,target,prefix_sum):
#         for i in range(len(prefix_sum)-count):
#             if prefix_sum[count+i] - prefix_sum[i] >= target:
#                 return True
#         return False
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         prefix_sum = [0]
#         for i in range( len(nums)):
#             prefix_sum.append(prefix_sum[i] + nums[i])
#         start,end = 0,len(prefix_sum)
#         res=0
#         while start < end:
#             mid = (start+end)//2
#             if self.isSubarraySum(mid,target,prefix_sum):
#                 res = mid
#                 end = mid
#             else:
#                 start = mid + 1
#         return res
# print(Solution().minSubArrayLen(target = 7, nums = [1,2,5]))


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        l = 0
        cSum = 0
        for r in range(len(nums)):
            cSum += nums[r]

            while cSum >= target:
                result = min(result, r - l + 1)
                cSum -= nums[l]
                l += 1

        return 0 if result == float("inf") else result