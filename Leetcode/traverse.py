'''
Created on Mar. 1, 2022

@author: Anmol Nagpal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.val = []
        self.traverse(root)
        return len(set(self.val)) == 1
            
    def traverse(self, root):
        if(root is not None):
            self.val.append(root.val)
            self.traverse(root.left)
            self.traverse(root.right)