'''
Created on Oct. 11, 2022

@author: Anmol Nagpal
'''

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mapping = {}
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        for s in s1:
            if s in mapping:
                mapping[s] += 1
            else:
                mapping[s] = 1
        for s in s2:
            if s in mapping:
                mapping[s] += 1
            else:
                mapping[s] = 1
        output = []
        for key in mapping.keys():
            if mapping[key] == 1:
                output.append(key)
        return output