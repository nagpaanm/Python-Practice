'''
Created on Apr. 25, 2022

@author: Anmol Nagpal
'''

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dict_ = {}
        # O(n)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i + 1] in dict_:
                    dict_[nums[i + 1]] += 1
                else:
                    dict_[nums[i + 1]] = 1
        max_ = 0
        key_ = None
        # O(n)
        for key in dict_.keys():
            if dict_[key] > max_:
                max_ = dict_[key]
                key_ = key
        return key_