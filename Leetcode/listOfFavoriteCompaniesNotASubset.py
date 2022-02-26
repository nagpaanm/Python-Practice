'''
Created on Feb. 26, 2022

@author: Anmol Nagpal
'''

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        index_list = []
        #favoriteCompanies.sort(key=len)
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                is_subList = False
                if(i != j):
                    if self.isSublist(favoriteCompanies[i], favoriteCompanies[j]):
                        is_subList = True
                        break
            if not is_subList:
                index_list.append(i)
        return index_list
    
    def isSublist(self, list1, list2):
        for element in list1:
            if element not in list2:
                return False
        return True