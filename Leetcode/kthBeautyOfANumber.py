'''
Created on Jun. 20, 2022

@author: Anmol Nagpal
'''

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        total = 0
        
        #O(n)
        for i in range(len(str(num)) - k + 1):
            num_str = str(num)[i:k + i]
            if int(num_str) != 0 and num % int(num_str) == 0:
                total +=1
        return total