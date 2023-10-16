'''
Created on May 9, 2022

@author: Anmol Nagpal
'''

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if s[0:len(word)] == word:
                count += 1
        return count