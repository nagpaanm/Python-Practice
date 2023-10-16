'''
Created on Apr. 24, 2022

@author: Anmol Nagpal
'''

class Solution:
    def interpret(self, command: str) -> str:
        dict_ = {"G":"G","()":"o","(al)":"al"}
        new_str = ""
        i = 0
        # O(n)
        while i < len(command):
            print(new_str)
            if command[i] in dict_.keys():
                new_str += dict_[command[i]]
                i += 1
            else:
                temp_str = command[i]
                # O(4)
                while temp_str not in dict_.keys():
                    i += 1
                    temp_str += command[i]
                new_str += dict_[temp_str]
                i += 1
        return new_str