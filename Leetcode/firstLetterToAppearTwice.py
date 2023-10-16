'''
Created on Sep. 20, 2022

@author: Anmol Nagpal
'''

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mapping = {}
        for char in s:
            if char in mapping:
                return char
            mapping[char] = 1