'''
Created on Feb. 25, 2022

@author: anmol nagpal
'''

"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses (
 '(' or ')', in any positions ) so that the resulting parentheses string is 
 valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, 
or It can be written as (A), where A is a valid string.
"""

# runtime O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        new_string = ""
        stack = []
        # O(n)
        for char in s:
            #print(new_string)
            if(char == "("):
                stack.append(char)
                new_string += char
            elif(char == ")"):
                if(len(stack) != 0):
                    new_string += char
                    stack.pop(len(stack) - 1)
            else:
                new_string += char
        # O(n)
        while len(stack) != 0:
            index = new_string.rfind("(")
            new_string = new_string[:index] + new_string[index + 1:]
            stack.pop(len(stack) - 1)
        return new_string
                