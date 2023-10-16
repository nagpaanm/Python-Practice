'''
Created on Feb. 26, 2022

@author: Anmol Nagpal
'''

"""
Given the array favoriteCompanies where favoriteCompanies[i] is the list of 
favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset 
of any other list of favorites companies. You must return the indices in 
increasing order.
"""

# runtime = O(n^2)
# space = O(n)
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        index_list = []
        set_list = {sub_list: set(element) for sub_list, element in enumerate(favoriteCompanies)}
        # O(n) 
        for i in range(len(set_list)):
            # O(n)
            for j in range(len(set_list)):
                is_subList = False
                if(i != j):
                    if set_list[i].intersection(set_list[j]) == set_list[i]:
                        is_subList = True
                        break
            if not is_subList:
                index_list.append(i)
        return index_list