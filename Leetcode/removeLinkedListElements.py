'''
Created on Apr. 5, 2022

@author: Anmol Nagpal
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ptr = head
        prev = None
        if(ptr == None):
            return head
        while(ptr != None):
            if(ptr.val == val):
                if prev != None:
                    while(ptr.next != None and ptr.next.val == val):
                        ptr = ptr.next
                    prev.next = ptr.next
                    prev = prev.next
                else:
                    head = ptr.next
            else:
                prev = ptr
            ptr = ptr.next
        return head
        