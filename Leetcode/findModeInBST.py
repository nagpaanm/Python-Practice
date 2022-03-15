'''
Created on Mar. 15, 2022

@author: Anmol Nagpal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dict_ = {}
        self.dfs(root)
        max_ = 0
        result = [0]
        for key in self.dict_.keys():
            if(self.dict_[key] > max_):
                result[0] = key
                max_ = self.dict_[key]
        for key in self.dict_.keys():
            if(self.dict_[key] == max_ and key != result[0]):
                result.append(key)
        return result
    
    def dfs(self, root):
        if(root is None):
            return
        if root.val in self.dict_:
            self.dict_[root.val] += 1
        else:
            self.dict_[root.val] = 1
        self.dfs(root.left)
        self.dfs(root.right)