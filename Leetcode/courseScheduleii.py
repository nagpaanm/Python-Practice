'''
Created on Feb. 20, 2022

@author: Anmol Nagpal
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = list()
        if(len(prerequisites) == 0):
            return [item for item in range(numCourses)]
        for lst in prerequisites:
            if lst[0] not in result:
                result.append(lst[0])
            if lst[1] not in result:
                result.append(lst[1])
        result = sorted(result)
        return result