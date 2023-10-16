'''
Created on Mar. 19, 2022

@author: Anmol Nagpal
'''

"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the 
matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element 
in its row and maximum in its column.
"""

import numpy as np
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        transposed = np.array(matrix).transpose()
        result = []
        for i in range(len(matrix)):
            x = min(matrix[i])
            index = matrix[i].index(x)
            y = max(transposed[index])
            if(x == y):
                result.append(x)
        return result