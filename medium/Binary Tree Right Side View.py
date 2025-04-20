from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    depth = 0

    def dfs(self, root, depth,res):
        if root:
            res[depth] = root.val
            if root.left == None and root.right == None:
                return list(res.values())
            self.dfs(root.left, depth + 1,res)
            self.dfs(root.right, depth + 1,res)
        return list(res.values())

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root,0,{})
print(Solution().rightSideView(TreeNode(1)))