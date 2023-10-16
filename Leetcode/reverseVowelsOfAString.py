'''
Created on Oct. 18, 2022

@author: Anmol Nagpal
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a":0, "e":0, "i":0, "o":0, "u":0, "A":0, "E":0, "I":0, "O":0, "U":0}
        place = ""
        
        # O(n)
        for char in s:
            if char in vowels:
                place += char
        place = place[::-1]
        counter = 0
        reverse = ""
        # O(n)
        for i in range(len(s)):
            if s[i] in vowels:
                reverse += place[counter]
                counter += 1
            else:
                reverse += s[i]
        return reverse
