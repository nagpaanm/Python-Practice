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
            pa = True
            #print(binaryArr)
            if(flips[i] < maxFound or flips[i] == maxFound + 1):
                #if "".join(str(item) for item in binaryArr[0:maxFound]) == "1" * maxFound: 
                summed =[item for item in binaryArr[0:maxFound]]
                if sum(summed) == maxFound:
                    total += 1
            maxFound = max(maxFound, flips[i])
        return total