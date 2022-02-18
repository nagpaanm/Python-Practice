'''
Created on Feb. 17, 2022

@author: Anmol Nagpal
'''

"""
Given a string s, check if it can be constructed by taking a substring of it and 
appending multiple copies of the substring together.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        else:
            i = 0
            j = 1
            while(j <= len(s)):
                substring = s[i:j]
                if len(s) % len(substring) == 0:
                    sub = substring
                    while(len(sub) < len(s)):
                        sub += substring
                        #print(sub)
                    if sub == s:
                        return True
                j += 1
                if j - i > len(s) / 2:
                    i += 1
            return False