'''
Created on Apr. 24, 2022

@author: Anmol Nagpal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = []
        # O(n)
        def inorder(node):
            if(node):
                inorder(node.left)
                lst.append(node)
                inorder(node.right)
        inorder(root)
        # O(n)
        for i in range(len(lst) - 1):
            lst[i].right = lst[i + 1]
            lst[i].left = None
        lst[len(lst) - 1].left = None
        return lst[0]