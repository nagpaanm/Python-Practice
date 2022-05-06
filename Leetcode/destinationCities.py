'''
Created on May 5, 2022

@author: Anmol Nagpal
'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mapping = {}
        # O(n)
        for combo in paths:
            mapping[combo[0]] = combo[1]
        # O(n)
        for val in mapping.values():
            if val not in mapping.keys():
                return val