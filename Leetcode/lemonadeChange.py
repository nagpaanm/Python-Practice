'''
Created on May 14, 2022

@author: Anmol Nagpal
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        # O(n)
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
                if(fives < 0):
                    return False
            else: # bill == 20
                twenties += 1
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif tens == 0 and fives >= 3:
                    fives -= 3
                else:
                    return False
        return True