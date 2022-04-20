'''
Created on Apr. 20, 2022

@author: nagpa
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        i1 = -1
        i2 = -1
        # O(n)
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                if i1 == -1:
                    i1 = i
                else:
                    i2 = i
        if(i1 == -1 and i2 == -1):
            return False
        if(i1 == -1 or i2 == -1):
            return False
        c1 = s1[i1]
        c2 = s1[i2]
        new_str = ""
        # O(n)
        for i in range(len(s2)):
            if(i == i1):
                new_str += c2
            elif (i == i2):
                new_str += c1
            else:
                new_str += s1[i]
        return new_str == s2