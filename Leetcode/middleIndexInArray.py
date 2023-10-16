# O(n^2)

class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            left_side = 0
            right_side = 1
            if i == 0:
                right_side = sum(nums[i + 1:])
                left_side = 0
            elif i == len(nums) - 1:
                right_side = 0
                left_side = sum(nums[:i])
            else:
                right_side = sum(nums[i + 1:])
                left_side = sum(nums[:i])
            if left_side == right_side:
                return i
        return -1