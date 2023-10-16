'''
Created on Aug. 10, 2022

@author: Anmol Nagpal
'''

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapping = {}
        #O(n)
        for x in arr1:
            if x in mapping:
                mapping[x] += 1
            else:
                mapping[x] = 1
        return_list = []
        last = []
        #O(n * m)
        for x in arr2:
            for i in range(mapping[x]):
                return_list.append(x)
            del mapping[x]
        back_end = []
        # O(n * m)
        for key in mapping.keys():
            for i in range(mapping[key]):
                back_end.append(key)
        #O(nlogn)
        back_end.sort()
        return return_list + back_end