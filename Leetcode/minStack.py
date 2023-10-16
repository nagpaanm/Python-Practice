'''
Created on May 6, 2022

@author: Anmol Nagpal
'''

class MinStack:
    
    def __init__(self):
        self.head = None
        
    def push(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(val, self.getMin()), self.head)
    
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min

class Node:
    def __init__(self, val, min_, next_):
        self.val = val
        self.min = min_
        self.next = next_

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()