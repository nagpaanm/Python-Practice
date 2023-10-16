'''
Created on Sep. 17, 2022

@author: Anmol Nagpal
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #binary search
        i = 0
        j = n
        while (i <= j):
            m = (i + j) / 2
            if isBadVersion(m):
                j = int(m - 1)
            else:
                i = int(m + 1)
        return i

def isBadVersion(n):
    pass 
