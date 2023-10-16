'''
Created on Mar. 3, 2022

@author: Anmol Nagpal
'''


"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

# runtime - O(n)
#space time - O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict_ = {}
        total = 0;
        for i in range(len(nums)):
            if nums[i] in dict_:
                if(dict_[nums[i]] == 1):
                    total += 1
                else:
                    total += dict_[nums[i]]
                dict_[nums[i]] += 1
            else:
                dict_[nums[i]] = 1
        
        return total