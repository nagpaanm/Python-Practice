'''
Created on Aug. 7, 2022

@author: Anmol Nagpal
'''

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        output = []
        totala = sum([x for x in aliceSizes])
        totalb = 0
        mapping = {}
        for x in bobSizes:
            totalb += x
            mapping[x] = 0
        for i in range(len(aliceSizes)):
            y = aliceSizes[i] - ((totala - totalb)/2)
            if y in mapping:
                return [aliceSizes[i], y]
        return output