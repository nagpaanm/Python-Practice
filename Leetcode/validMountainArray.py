'''
Created on Feb. 16, 2023

@author: Anmol Nagpal
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        is_ascending = None
        is_descending = None
        # O(n)
        for i in range(len(arr) - 1):
            print(arr[i])
            if arr[i] < arr[i + 1] and (is_ascending == None or is_ascending):
                is_ascending = True
            elif arr[i] > arr[i + 1] and is_ascending != None and (is_descending == None or is_descending):
                is_ascending = False
                is_descending = True
            else:
                return False
        if is_descending == None:
            return False
        return True