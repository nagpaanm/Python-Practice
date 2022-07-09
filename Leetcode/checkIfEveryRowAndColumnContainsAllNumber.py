'''
Created on Jul. 9, 2022

@author: Anmol Nagpal
'''

import numpy as np

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix[0])
        standard = [i for i in range(1, n + 1)]
        for i in range(n):
            if len(set(standard).symmetric_difference(set(matrix[i]))) != 0:
                return False
        transpose = np.array(matrix)
        transpose = transpose.T
        for i in range(n):
            if len(set(standard).symmetric_difference(set(transpose[i]))) != 0:
                return False
        return True