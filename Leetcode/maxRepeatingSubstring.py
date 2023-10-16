'''
Created on May 15, 2022

@author: Anmol
'''

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence == word:
            return 1
        total = 0
        index = 0
        temp_total = 0
        stored_index = 0
        while index < len(sequence):
            if sequence[index:index + len(word)] == word:
                temp_total += 1
                index += len(word)
            else:
                total = max(total, temp_total)
                temp_total = 0
                stored_index += 1
                index = stored_index
        return max(total, temp_total)