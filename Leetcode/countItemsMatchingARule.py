'''
Created on Mar. 27, 2022

@author: Anmol Nagpal
'''

# O(n) time
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        total = 0
        dict_ = {"type":0, "color":1, "name":2}
        index = dict_[ruleKey]
        for item in items:
            if(item[index] == ruleValue):
                total +=1
        return total