from typing import List


# class Solution:
#     def binary_search(self,list,target):
#         start,end = 0, len(list)-1
#         while start <=end:
#             mid = (start+end)//2
#             if list[mid] == target:
#                 return True
#             elif list[mid] < target:
#                 start = mid+1
#             elif list[mid] > target:
#                 end = mid-1
#         return False
#
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for i in range(len(matrix)-1,-1,-1):
#             if self.binary_search(matrix[i],target):
#                 return True
#         return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        cou=0
        while r < m and c >= 0:
            if target > matrix[r][c]:
                r += 1
                cou+=1
                print(cou)
            elif target < matrix[r][c]:
                c -= 1
                cou+=1
                print(cou)
            else: return True
        return False


print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 100))