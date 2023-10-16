'''
Created on Nov. 16, 2022

@author: Anmol Nagpal
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n
        max_ = None
        while (left <= right):
            mid = (left + right) // 2
            if (mid * (mid + 1)) // 2 <= n : #Gauss summation
                max_ = mid
                left = mid + 1
            else:
                right = mid - 1
        return max_