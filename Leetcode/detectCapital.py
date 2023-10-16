'''
Created on Jan. 26, 2023

@author: Anmol Nagpal
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower() or word == word.capitalize():
            return True
        return False