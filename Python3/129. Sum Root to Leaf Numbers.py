# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import  Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        current = 0

        def dfs(node, current):
            if not node:
                return 0

            current = current*10 + node.val

            if not node.right and not node.left:
                return current

            return dfs(node.right, current) + dfs(node.left , current)
        
        return dfs(root , 0)