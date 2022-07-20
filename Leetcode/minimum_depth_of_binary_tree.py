'''
Created on Jul. 19, 2022

@author: Anmol Nagpal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMinDepth(root)
    
    def getMinDepth(self, root):
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return self.getMinDepth(root.right) + 1
        if root.right == None:
            return self.getMinDepth(root.left) + 1
        return min(self.getMinDepth(root.left), self.getMinDepth(root.right)) + 1