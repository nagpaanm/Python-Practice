'''
Created on Jun. 3, 2022

@author: Anmol Nagpal
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        # O(logn)
        while (left <= right):
            mid = int((left + right) / 2)
            if mid * mid == num:
                return True
            if mid * mid > num:
                right = mid - 1
            if mid * mid < num:
                left = mid + 1
        return False