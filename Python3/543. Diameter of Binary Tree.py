# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            leftheight = height(node.left)
            rightheight = height(node.right)

            self.diameter = max(self.diameter , leftheight + rightheight)

            return 1 + max(leftheight , rightheight)
        height(root)
        return self.diameter
        