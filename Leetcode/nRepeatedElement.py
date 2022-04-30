'''
Created on Apr. 30, 2022

@author: Anmol Nagpal
'''

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mapping = {}
        halved = len(nums) / 2
        # runtime -> O(n)
        # space complexity -> O(n)
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
            if mapping[num] == halved:
                return num