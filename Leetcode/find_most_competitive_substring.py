'''
Created on Feb. 27, 2022

@author: Anmol Nagpal
'''

"""
Given an integer array nums and a positive integer k, return the most 
competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some 
(possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b 
(of the same length) if in the first position where a and b differ, subsequence 
a has a number less than the corresponding number in b. For example, [1,3,4] is 
more competitive than [1,3,5] because the first position they differ is at the 
final number, and 4 is less than 5.
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        output = []
        index = -1
        m = k
        if(k == len(nums)):
            return nums
        while(len(output) < k):
            index = self.find_lowest(nums, index)
            output.append(nums[index])
            m -= 1
        return output
    
    def find_lowest(self, list1, index, m):
        smallest = 10000000001
        for i in range(index + 1, len(list1)):
            if(list1[i] == 0 and len(list1) - i >= m):
                return i
            if(list1[i] < smallest and len(list1) - i >= m):
                smallest = list1[i]
                index = i
            if(len(list1) - i < m):
                break
        return index