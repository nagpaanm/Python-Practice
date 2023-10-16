'''
Created on Aug. 21, 2022

@author: Anmol Nagpal
'''

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        total = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                if total > 0:
                    total -= 1
            elif logs[i] == "./":
                total -= 0
            else:
                total += 1
        return total