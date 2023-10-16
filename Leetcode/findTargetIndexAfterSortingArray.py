'''
Created on Nov. 23, 2022

@author: Anmol Nagpal
'''

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        index = None
        if target in nums:
            index = nums.index(target)
            indices.append(index)
            while index < len(nums) -1 and nums[index + 1] == target:
                indices.append(index + 1)
                index += 1
        return indices