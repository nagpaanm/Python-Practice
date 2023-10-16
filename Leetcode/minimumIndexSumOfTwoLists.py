'''
Created on Mar. 13, 2022

@author: Anmol Nagpal
'''

"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both 
have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index 
sum. If there is a choice tie between answers, output all of them with no order 
requirement. You could assume there always exists an answer.
"""

#O(n) runtime
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        #O(n)
        list3 = list(set(list1).intersection(set(list2)))
        output = []
        index_sum_list = []
        dict_ = {}
        # O(n)
        for item in list3:
            sum_ = list1.index(item) + list2.index(item)
            if sum_ in dict_:
                dict_[sum_].append(item)
            else:
                dict_[sum_] = [item]
            index_sum_list.append(sum_)
        output.extend(dict_[min(index_sum_list)])
        return output