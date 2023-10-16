'''
Created on Oct. 8, 2022

@author: Anmol Nagpal
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            i = 0
            j = len(s) - 1
            while (i < j):
                if s[i] != s[j]:
                    delete_i = s[i + 1:j + 1]
                    delete_j = s[i:j]
                    return delete_i == delete_i[::-1] or delete_j == delete_j[::-1]
                i +=1 
                j -= 1
        return True