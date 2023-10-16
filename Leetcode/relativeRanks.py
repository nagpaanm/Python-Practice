'''
Created on Jul. 16, 2022

@author: Anmol Nagpal
'''

class Solution:
    # O(nlogn) + O(n) = O(nlogn)
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        print(score)
        if len(score) == 0:
            return []
        elif len(score) == 1:
            return ["Gold Medal"]
        elif len(score) == 2:
            if score[0] > score[1]:
                score[0] = "Gold Medal"
                score[1] = "Silver Medal"
            else:
                score[1] = "Gold Medal"
                score[0] = "Silver Medal"
        else:
            lst = score.copy()
            # O(nlogn)
            lst.sort()
            score[score.index(lst[-1])] = "Gold Medal"
            score[score.index(lst[-2])] = "Silver Medal"
            score[score.index(lst[-3])] = "Bronze Medal"
            counter = 4
            # O(n)
            for i in range(len(lst) - 4, -1, -1):
                score[score.index(lst[i])] = str(counter)
                counter += 1
        return score
    