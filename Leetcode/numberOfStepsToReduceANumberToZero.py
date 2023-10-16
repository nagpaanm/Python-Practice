'''
Created on Jul. 1, 2022

@author: Anmol Nagpal
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        # O(logn)
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            steps += 1
        return steps