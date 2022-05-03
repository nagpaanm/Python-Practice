'''
Created on May 3, 2022

@author: Anmol Nagpal
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        ans.append(set(nums1) - set(nums2))
        ans.append(set(nums2) - set(nums1))
        return ans