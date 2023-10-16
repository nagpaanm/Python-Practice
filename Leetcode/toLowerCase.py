'''
Created on Feb. 10, 2023

@author: Anmol Nagpal
'''

class Solution:
    def toLowerCase(self, s: str) -> str:
        mapping = {"A":"a",
                    "B":"b",
                    "C":"c",
                    "D":"d",
                    "E":"e",
                    "F":"f",
                    "G":"g",
                    "H":"h",
                    "I":"i",
                    "J":"j",
                    "K":"k",
                    "L":"l",
                    "M":"m",
                    "N":"n",
                    "O":"o",
                    "P":"p",
                    "Q":"q",
                    "R":"r",
                    "S":"s",
                    "T":"t",
                    "U":"u",
                    "V":"v",
                    "W": "w",
                    "X": "x",
                    "Y": "y",
                    "Z": "z"}
        new_string = ""
        # O(n)
        for char in s:
            if char in mapping:
                new_string += mapping[char]
            else:
                new_string += char
        return new_string