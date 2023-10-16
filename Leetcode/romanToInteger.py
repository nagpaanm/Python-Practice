'''
Created on Aug. 24, 2022

@author: Anmol Nagpal
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        length = len(s)
        total = 0
        i = 0
        # O(N)
        while(i < length):
            if (i == length - 1):
                total += mapping[s[i]]
            else:
                pair = s[i] + s[i + 1]
                i += 1
                if pair == "IV":
                    total += 4
                elif pair == "IX":
                    total += 9
                elif pair == "XL":
                    total += 40
                elif pair == "XC":
                    total += 90
                elif pair == "CD":
                    total += 400
                elif pair == "CM":
                    total += 900
                else:
                    i -= 1
                    total += mapping[s[i]]
            i +=1
                
        return total