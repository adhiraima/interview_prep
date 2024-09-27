from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node, depth):
            if not node:
                return depth
            return max(height(node.left, depth + 1), height(node.right, depth + 1))

        if not root:
            return True
        
        q = deque()
        q.append(root)
        count = 1
        while q:
            print("Iteration# ", count)
            node = q.popleft()
            if not node:
                return True

            l_height = height(node.left, 0)
            r_height = height(node.right, 0)

            if abs(l_height - r_height) > 1:
                return False
            
            if node:
                q.append(node.left)
                q.append(node.right)
            
            count += 1
        return True 
        