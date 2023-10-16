'''
Created on May 29, 2022

@author: Anmol Nagpal
'''

class Solution:
    # O(n) time
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            m = target - nums[i]
            if m in mapping:
                return [mapping[m], i]
            else:
                mapping[nums[i]] = i
        