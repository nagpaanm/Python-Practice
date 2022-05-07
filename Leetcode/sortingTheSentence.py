'''
Created on May 7, 2022

@author: Anmol Nagpal
'''

# O(nlogn) + O(2n)
class Solution:
    def sortSentence(self, s: str) -> str:
        list_ = s.split(" ")
        mapping = {}
        list_sorted = []
        # O(n)
        for word in list_:
            list_sorted.append(int(word[len(word) - 1]))
            mapping[int(word[len(word) - 1])] = word[:len(word) - 1]
        # O(nlogn)
        list_sorted.sort()
        new_str = ""
        # O(n)
        for num in list_sorted:
            new_str += mapping[num] + " "
        return new_str.strip( " ")
        