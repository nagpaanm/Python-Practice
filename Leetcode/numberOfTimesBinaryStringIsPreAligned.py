'''
Created on Feb. 18, 2022

@author: nagpa
'''

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        binaryArr = [0] * len(flips)
        total = 0
        maxFound = 0;
        for i in range(len(flips)):
            binaryArr[flips[i] - 1] = 1
            maxFound = max(maxFound, flips[i])
            if "".join(str(item) for item in binaryArr[0:maxFound]) == "1" * maxFound:  
                total += 1
        return total