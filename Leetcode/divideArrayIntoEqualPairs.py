class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        # O(n)
        for key in mapping.keys():
            if mapping[key] % 2 != 0:
                return False
        return True