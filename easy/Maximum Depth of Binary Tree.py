# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode],depth=0) -> int:
        pointer=root
        while pointer:
            depth+=1
            return max(self.maxDepth(pointer.left,depth),self.maxDepth(pointer.right,depth))
        return depth
