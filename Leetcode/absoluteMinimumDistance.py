'''
Created on Mar. 23, 2022

@author: Anmol Nagpal
'''

# O(nlogn) runtime
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if(len(arr) < 2):
            return [[]]
        result = []
        min_ = 10000001
        index = 0
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) < min_:
                min_ = abs(arr[i] - arr[i + 1])
                index = i
        result.append([arr[index], arr[index + 1]])
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == min_ and i != index:
                result.append([arr[i], arr[i + 1]])
        return result