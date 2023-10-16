'''
Created on Jan. 19, 2023

@author: Anmol Nagpal
'''

class Solution:
    # O(n)
    def digitCount(self, num: str) -> bool:
        mapping = {}
        # O(n)
        for i in range(len(num)):
            occurence = num[i]
            if i in mapping:
                mapping[i] += occurence
            else:
                mapping[i] = occurence
        # O(n)
        for key in mapping.keys():
            if num.count(str(key)) != int(mapping[key]):
                return False
        return True