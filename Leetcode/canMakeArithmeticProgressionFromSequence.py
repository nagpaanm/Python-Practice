'''
Created on Oct. 15, 2022

@author: Anmol Nagpal
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        solid = True
        diff = None
        # n(nlogn) 
        arr.sort()
        # (logn)
        for i in range(len(arr) - 1):
            if diff is None:
                diff = abs(arr[i + 1] - arr[i])
            else:
                if abs(arr[i + 1] - arr[i]) != diff:
                    return False
        return True