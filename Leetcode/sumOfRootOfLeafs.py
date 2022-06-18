'''
Created on Jun. 18, 2022

@author: Anmol Nagpal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        storage = []
        string = ""
        self.getPaths(root, storage, string)
        return self.convertToDecimal(storage)
    
    def getPaths(self, root, storage, string):
        if root is None:
            return
        string += str(root.val)
        if root.left == None and root.right == None:
            storage.append(string)
        self.getPaths(root.left, storage, string)
        self.getPaths(root.right, storage, string)
    
    def convertToDecimal(self, storage):
        total = 0
        for item in storage:
            total += int(item, 2)
        return total