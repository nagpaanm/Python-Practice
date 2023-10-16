'''
Created on Jan. 13, 2023

@author: Anmol Nagpal
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        m = 2
        iterator = 1
        # O(n^2)
        while(True):
            val = m ** iterator
            if val == n:
                return True
            if val > n:
                return False
            iterator += 1