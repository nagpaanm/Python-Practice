'''
Created on Jul. 24, 2022

@author: Anmol Nagpal
'''

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if(len(s) < 3):
            return []
        tmp = []
        storage = []
        curr = s[0]
        #O(n)
        for i in range(0, len(s)):
            if s[i] == curr:
                if(len(tmp) == 0):
                    tmp.append(i)
                if i == len(s) - 1:
                    tmp.append(i)
                    if(tmp[1] - tmp[0] >= 2):
                        storage.append(tmp)
            else:
                if(len(tmp) == 1):
                    tmp.append(i - 1)
                    if(tmp[1] - tmp[0] >= 2):
                        storage.append(tmp)
                tmp = [i]
                curr = s[i] 
        return storage