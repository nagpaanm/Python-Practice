'''
Created on Apr. 11, 2022

@author: nagpa
'''

import re

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # O(n)
        list_ = re.findall("\d+", s)
        prev = None
        
        # O(n)
        for num in list_:
            if prev == None:
                prev = int(num)
            else:
                if int(num) <= prev:
                    return False
            prev = int(num)
        return True