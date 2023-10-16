'''
Created on Mar. 20, 2022

@author: Anmol Nagpal
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(" ")
        if(len(word_list) != len(pattern)):
            return False
        mapping = {}
        values = []
        for i in range(len(pattern)):
            if word_list[i] in mapping:
                if pattern[i] not in mapping[word_list[i]] and mapping[word_list[i]][0] != pattern[i]:
                    return False
            else:
                if(pattern[i] in values):
                    return False
                mapping[word_list[i]] = [pattern[i]]
            values.append(pattern[i])
        return True