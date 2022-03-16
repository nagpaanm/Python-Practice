'''
Created on Mar. 16, 2022

@author: Anmol Nagpal
'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list_ = [""] * len(s)
        for i in range(len(s)):
            list_[indices[i]] = s[i]
        return "".join(list_)