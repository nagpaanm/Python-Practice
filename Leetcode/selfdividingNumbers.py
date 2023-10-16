'''
Created on Jun. 15, 2022

@author: Anmol Nagpal
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right + 1):
            if self.is_self_dividing(i):
                arr.append(i)
        return arr
    
    def is_self_dividing(self, i):
        for char in str(i):
            if int(char) == 0:
                return False
            if i % int(char) != 0:
                return False
        return True