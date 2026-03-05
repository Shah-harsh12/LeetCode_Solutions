# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result
        queue = [root]

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level[-1])

        return result