'''
Created on Sep. 24, 2022

@author: Anmol Nagpal
'''

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = []
        output = []
        length = len(s)
        # O(n)
        for i in range(length):
            if s[i] == c:
                indices.append(i)
        counter = 0
        # O(n)
        for i in range(length):
            if s[i] == c:
                output.append(0)
                counter +=1
            else:
                if(counter == 0):
                    output.append(abs(indices[counter] - i))
                else:
                    if counter >= len(indices):
                        output.append(abs(indices[counter - 1] - i))
                    else:
                        if abs(indices[counter] - i ) < abs(indices[counter - 1] - i):
                            output.append(abs(indices[counter] - i))
                        else:
                            output.append(abs(indices[counter - 1] - i))
        return output