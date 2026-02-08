from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,root,result):
        if root:
            self.solve(root.left,result)
            result.append(root.val)
            self.solve(root.right,result)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.solve(root, result)
print(Solution().inorderTraversal(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)))))