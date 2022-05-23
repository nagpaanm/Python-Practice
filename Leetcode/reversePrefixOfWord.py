'''
Created on May 23, 2022

@author: Anmol Nagpal
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        if ch in word:
            index = word.index(ch)
        if index == -1:
            return word
        else:
            """
            reverse = ""
            for i in range(index, -1, -1):
                reverse += word[i]
            return reverse + word[index + 1:]
            """
            reverse = word[0: index + 1]
            return reverse[::-1] + word[index + 1:]