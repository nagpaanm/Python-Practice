'''
Created on Jun. 4, 2022

@author: Anmol Nagpal
'''

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        # O(n^2)
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                x = math.sqrt((i * i) + (j * j))
                if x.is_integer() and x <= n:
                    count += 2 
        return count