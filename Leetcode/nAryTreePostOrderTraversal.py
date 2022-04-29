'''
Created on Apr. 29, 2022

@author: Anmol Nagpal
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# O(n) runtime
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.list_ = []
        def pOrder(root):
            if root:
                for child in root.children:
                    pOrder(child)
                    self.list_.append(child.val)
        pOrder(root)
        if root:
            self.list_.append(root.val)
        return self.list_