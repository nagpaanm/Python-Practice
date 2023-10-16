'''
Created on Aug. 28, 2022

@author: Anmol Nagpal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        return self.sumLefts(root, None)
    
    def sumLefts(self, root, prev):
        if root == None:
            return 0
        if root.left == None and root.right == None and prev == "left":
            return root.val
        total = 0
        total += self.sumLefts(root.left, "left") + self.sumLefts(root.right, "right")
        return total