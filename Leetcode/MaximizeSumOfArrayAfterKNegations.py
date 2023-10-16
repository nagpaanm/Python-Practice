'''
Created on Nov. 9, 2022

@author: Anmol Nagpal
'''

class Solution:
    # O(n * k)
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        tracker = 0
        # O(k)
        while tracker < k:
            # O(n)
            min_ = min(nums)
            index = nums.index(min_)
            nums[index] = nums[index] *  -1
            tracker += 1
        return sum(nums)
