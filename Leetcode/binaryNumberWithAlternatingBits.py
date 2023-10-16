'''
Created on Jan. 6, 2023

@author: Anmol Nagpal
'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        br = str(bin(n)[2:])
        last_bit = None
        # O(n) runtime
        for char in br:
            if last_bit == None:
                last_bit = char
            else:
                if char == last_bit:
                    return False
                else:
                    last_bit = char
        return True