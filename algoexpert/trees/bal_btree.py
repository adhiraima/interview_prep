# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
        l_height = height(root.left, 0)
        r_height =  height(root.right, 0)

        return abs(l_height - r_height) <= 1 
        