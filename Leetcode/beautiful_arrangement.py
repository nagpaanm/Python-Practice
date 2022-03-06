'''
Created on Mar. 5, 2022

@author: Anmol Nagpal
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        arr = [i for i in range(n + 1)]
        self.total = 0;
        self.recurse(arr, len(arr) - 1)
        return self.total
    
    def recurse(self, arr, index):
        if(self.check_beautiful(arr)):
            self.total += 1
        for i in range(len(arr)):
            n = arr.pop(0)
            
    
    def check_beautiful(self, arr):
        for i in range(len(arr)):
            if(arr[i] % (i + 1) != 0 or (i + 1) % arr[i] != 0):
                return False
        return True