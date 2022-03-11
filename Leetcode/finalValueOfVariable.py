'''
Created on Mar. 11, 2022

@author: Anmol Nagpal
'''

"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return 
the final value of X after performing all the operations.
"""

# O(n) runtime. O(1) spacetime
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        dict_ = {"--X": -1, "X--": -1, "++X": 1, "X++":1}
        for operation in operations:
            total += dict_[operation]
        return total
