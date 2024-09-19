# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.depth(root, 0)
        return self.bfs(root)

    
    def depth(self, root, depth) -> int:
        if not root:
            return depth
        
        return 1 + max(self.depth(root.left, depth), 
                    self.depth(root.right, depth))


    def bfs(self, root):
        if not root:
            return 0
        que = deque([root])
        level = 0
        while que:
            for i in range(0, len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
        return level
    
print(Solution().maxDepth(TreeNode()))