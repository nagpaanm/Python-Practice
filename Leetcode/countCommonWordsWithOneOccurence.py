'''
Created on May 16, 2022

@author: Anmol Nagpal
'''

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        mapping = {}
        total = 0
        # O(n)
        for word in words1:
            if word in mapping:
                mapping[word] = [False, mapping[word][1] + 1]
            else:
                mapping[word] = [False, 1]
        # O(n)
        for word in words2:
            if word in mapping:
                mapping[word] = [True, mapping[word][1] + 1]
        # O(n)
        for keys in mapping.keys():
            if mapping[keys][1] == 2 and mapping[keys][0] == True:
                total += 1
        return total
