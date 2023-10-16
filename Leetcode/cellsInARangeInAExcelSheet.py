'''
Created on Apr. 12, 2022

@author: Anmol Nagpal
'''

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        listed = s.split(":")
        min_ = int(listed[0][1])
        max_ = int(listed[1][1])
        l1 = listed[0][0]
        output = []
        # O(n^m)
        while(l1 <= listed[1][0]):
            if(min_ != max_):
                m = min_
                while(m <= max_):
                    output.append(l1 + str(m))
                    m += 1
                n = ord(l1) + 1
                l1 = chr(n)
            else:
                output.append(l1 + str(min_))
                n = ord(l1) + 1
                l1 = chr(n)
        return output