'''
Created on Mar. 10, 2022

@author: Anmol Nagpal
'''

"""
Given an integer num, repeatedly add all its digits until the result has 
only one digit, and return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while(num >= 10):
            num = int(num / 10) + (num % 10)
        return num