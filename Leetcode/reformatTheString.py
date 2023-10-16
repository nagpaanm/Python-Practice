'''
Created on Aug. 17, 2022

@author: Anmol Nagpal
'''

class Solution:
    def reformat(self, s: str) -> str:
        reformatted = ""
        prev = None
        char_list = []
        num_list = []
        # O(n)
        for i in range(len(s)):
            if prev is None:
                prev = s[i]
                reformatted = prev
            else:
                if prev.isdigit() and not s[i].isdigit():
                    reformatted += s[i]
                elif not prev.isdigit() and s[i].isdigit():
                    reformatted += s[i]
                else:
                    reformatted = s[i]
                prev = s[i]
            if s[i].isdigit():
                num_list.append(s[i])
            else:
                char_list.append(s[i])
                
        if len(reformatted) == len(s):
            return reformatted
        else:
            if len(char_list) == len(num_list) or len(char_list) - 1 == len(num_list):
                return self.assemble_string(char_list, num_list)
            elif len(num_list) == len(char_list) or len(num_list) - 1 == len(char_list):
                return self.assemble_string(num_list, char_list)
            else:
                return ""
    
    def assemble_string(self, alpha, beta):
        assembler = ""
        # O(n)
        for i in range(len(alpha)):
            assembler += alpha[i]
            if i != len(beta):
                assembler += beta[i]
        return assembler
