# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            val = que_val.popleft()
            if not now.left and not now.right:
                if val == targetSum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + val)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + val)
        return False



