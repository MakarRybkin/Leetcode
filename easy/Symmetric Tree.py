from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_Same(self, p, q):
        return p.val == q.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        else:
            return self.is_Same(p, q) & self.isSameTree(p.left, q.right) & self.isSameTree(p.right, q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = root.right
        p = root.left
        return self.isSameTree( p, q)




print(Solution().isSymmetric(TreeNode(0,TreeNode(2,TreeNode(1)),TreeNode(2,None,TreeNode(1)))))
