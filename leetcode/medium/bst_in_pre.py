# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])

        def create_tree(preorder, inorder):
            if inorder:
                val = preorder.pop(0)
                index = inorder.index(val)
                node = TreeNode(val)
                node.left = create_tree(preorder, inorder[:index])
                node.right = create_tree(preorder, inorder[index+1:])
                return node

        return create_tree(preorder, inorder)
