'''
Created on May 4, 2022

@author: Anmol
'''

# O(n^2)
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        index = 0
        max_ = 0
        # O(n)
        for i in range(n):
            set_ = set()
            missing = 0
            # O(n)
            for j in range(i, n):
                if s[j] not in set_:
                    set_.add(s[j])
                    if (s[j].upper() not in set_) or (s[j].lower() not in set_):
                        missing += 1
                    else:
                        missing -= 1
                if missing == 0 and j - i + 1 > max_:
                    max_ = j - i + 1
                    index = i
        return s[index:index + max_]