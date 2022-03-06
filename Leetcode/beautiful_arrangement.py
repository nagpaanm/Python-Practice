'''
Created on Mar. 5, 2022

@author: Anmol Nagpal
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        arr = [i for i in range(1, n + 1)]
        if(n == 1):
            return 1
        self.total = 0
        self.recurse(arr)
        return self.total
    
    def recurse(self, arr):
        result = []
        if(len(arr) == 1):
            return [arr.copy()]
        for i in range(len(arr)):
            n = arr.pop(0)
            perms = self.recurse(arr)
            for perm in perms:
                perm.append(n)
                if self.check_beautiful(perm):
                    self.total +=1
            result.extend(perms)
            arr.append(n)
        return result
            
    def check_beautiful(self, arr):
        for i in range(len(arr)):
            if(arr[i] % (i + 1) != 0 and (i + 1) % arr[i] != 0):
                #print("{}, {}".format(i, arr[i]))
                return False
        return True