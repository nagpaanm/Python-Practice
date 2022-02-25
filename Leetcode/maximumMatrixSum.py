'''
Created on Feb. 24, 2022

@author: Anmol Nagpal
'''

"""
You are given an n x n integer matrix. You can do the following 
operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return 
the maximum sum of the matrix's elements using the operation mentioned above.
"""


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_total = 0
        neg_count = 0
        abs_min = inf
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                abs_min = min(abs_min, abs(matrix[i][j]))
                abs_total += abs(matrix[i][j])
                if(matrix[i][j]) < 0:
                    neg_count += 1
                    
        if neg_count % 2 == 0: # even number of negatives
            return abs_total
        else:
            # if odd number of negatives, at least one negative will always
            # be remaining
            return abs_total - abs_min*2 
        return total
    
