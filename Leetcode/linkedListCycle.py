'''
Created on Feb. 21, 2022

@author: Anmol Nagpal
'''

"""
Given head, the head of a linked list, determine if the linked list has a 
cycle in it.

There is a cycle in a linked list if there is some node in the list that 
can be reached again by continuously following the next pointer. Internally, 
pos is used to denote the index of the node that tail's next pointer is 
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


# O(1) space
# O(n) runtime

from ListNode import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        walker = head
        runner = head
        while(walker.next != None and runner != None and runner.next != None):
            walker = walker.next
            runner = runner.next.next
            if(walker == runner):
                return True
        return False