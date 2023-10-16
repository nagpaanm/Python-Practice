'''
Created on Dec. 16, 2022

@author: Anmol Nagpal
'''

class Solution:
    def secondHighest(self, s: str) -> int:
        max1 = None
        max2 = -1
        for char in s:
            if char.isdigit():
                num = int(char)
                if max1 == None:
                    max1 = num
                else:
                    if num > max1:
                        max2 = max1
                        max1 = num
                    if num < max1:
                        if max2 == -1:
                            max2 = num
                        else:
                            if num > max2:
                                max2 = num
        return max2