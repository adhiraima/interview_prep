# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_same_tree(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                return is_same_tree(left.left, right.right) and is_same_tree(left.right, right.left)
            return False
        
        return is_same_tree(root.left, root.right)
        