from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1=nums1[:m]
        arr2=nums2[:n]
        p1,p2=0,0
        while p1<len(arr1) and p2<len(arr2):
            if arr1[p1]<=arr2[p2]:
                nums1[p1+p2]=arr1[p1]
                p1+=1
            else:
                nums1[p1+p2]=arr2[p2]
                p2+=1
        while nums1 and nums2 and len(nums1)> p1+p2:
            nums1.pop()
        if len(nums1)< len(nums2)+len(nums1):
            nums1.extend(arr2[p2:len(arr2)])
            nums1.extend(arr1[p1:len(arr1)])
        return nums1
print(Solution().merge([1,2,4,5,6,0],5,[3],1))
