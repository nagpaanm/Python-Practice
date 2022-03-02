'''
Created on Mar. 1, 2022

@author: Anmol Nagpal
'''

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return False if self.traverse(root) == 0 else True
            
    def traverse(self, root):
        if root is None:
            return 1
        if(root.left is None and root.right is None):
            return 1
        if(root.left is not None):
            if(root.left.val == root.val):
                return 1 + self.traverse(root.left)
            else:
                return 0
        if(root.right is not None):
            if(root.right.val == root.val):
                return 1 + self.traverse(root.right)
            else:
                return 0