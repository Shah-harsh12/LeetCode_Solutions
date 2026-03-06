# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None

        def revpreorder(node):
            if not node:
                return
            revpreorder(node.right)
            revpreorder(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        
        revpreorder(root)

        