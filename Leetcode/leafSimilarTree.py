'''
Created on Jun. 12, 2022

@author: Anmol Nagpal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1 = []
        list2 = []
        if root1 == None and root2 == None:
            return True
        if (root1 == None and root2 != None) or (root2 == None and root1 != None):
            return False
        self.getLeaves(root1, list1)
        self.getLeaves(root2, list2)
        return list1 == list2
    
    def getLeaves(self, root, lst):
        if root.left == None and root.right == None:
            lst.append(root.val)
            return
        if root.left != None:
            self.getLeaves(root.left, lst)
        if root.right != None:
            self.getLeaves(root.right, lst)