'''
Created on Feb. 21, 2022

@author: Anmol Nagpal
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dp(target, 0, nums, len(nums) - 1, 0)
    
    def dp(self, target, total, nums, index, ways):
        if(index < 0):
            if(target == total):
                #ways += 1
                return 1
            return 0
        ways += self.dp(target, total + nums[index], nums, index - 1, ways)
        ways += self.dp(target, total - nums[index], nums, index - 1, ways)
        return ways