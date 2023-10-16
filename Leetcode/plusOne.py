'''
Created on Jun. 26, 2022

@author: Anmol Nagpal
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        # O(n)
        for num in digits:
            string += str(num)
        string = str(int(string) + 1)
        output = []
        # O(n)
        for char in string:
            output.append(int(char))
        return output
