from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_length = len(matrix)*len(matrix[0]) - 1
        start,end = 0, matrix_length
        while start<=end:
            mid = (start+end)//2
            if matrix[mid//len(matrix[0])][mid%len(matrix[0])] == target:
                print(mid%len(matrix))
                return True
            elif matrix[mid//len(matrix[0])][mid%len(matrix)] < target:
                start = mid+1
            elif matrix[mid//len(matrix[0])][mid%len(matrix)]>target:
                end = mid-1
        return False
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 6))

