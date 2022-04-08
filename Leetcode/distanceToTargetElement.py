'''
Created on Apr. 7, 2022

@author: Anmol Nagpal
'''

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        val = 10001
        # O(n) runtime
        for i in range(len(nums)):
            if nums[i] == target:
                val = min(abs(i - start), val)
        return val