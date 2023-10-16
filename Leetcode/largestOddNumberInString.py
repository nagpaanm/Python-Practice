'''
Created on May 13, 2022

@author: Anmol Nagpal
'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # O(n)
        for i in range(len(num) - 1, -1, -1):
            if num[i] != "" and int(num[i]) % 2 != 0:
                return num[0:i+1]
        return ""
 