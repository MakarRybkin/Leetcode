# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,root,result):
        if root:
            result.append(root.val)
            self.solve(root.left,result)
            self.solve(root.right,result)
        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.solve(root, result)

print(Solution().preorderTraversal(TreeNode(1, TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7))), TreeNode(3,None,TreeNode(8,TreeNode(9),None)))))
