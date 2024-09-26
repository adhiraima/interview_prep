# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root: TreeNode, height):
            if root:
                return max(depth(root.left, height + 1), depth(root.right, height + 1))
            return height
        
        return depth(root, 0)
        