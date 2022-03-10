'''
Created on Mar. 10, 2022

@author: Anmol Nagpal
'''

#O(m*n)
#sliding window technique
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        dict = {}
        dict["a"] = 0
        dict["e"] = 0
        dict["i"] = 0
        dict["o"] = 0
        dict["u"] = 0
        i = 0
        j = 0
        total = 0
        while(j < len(word)):
            if(word[j] in dict.keys()):
                dict[word[j]] += 1
                if(j - i >= 4):
                    substring = True
                    for str_ in dict.keys():
                        if dict[str_] == 0:
                            substring = False
                    if(substring):
                        total += 1
            if(word[j] not in dict.keys() or j == len(word) - 1):
                i += 1
                j = i - 1
                dict["a"] = 0
                dict["e"] = 0
                dict["i"] = 0
                dict["o"] = 0
                dict["u"] = 0
            j += 1
        return total