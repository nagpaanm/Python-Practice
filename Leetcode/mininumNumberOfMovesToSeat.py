'''
Created on Apr. 3, 2022

@author: nagpa
'''
# O(nlogn)
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # O(nlogn)
        seats.sort()
        # O(nlogn)
        students.sort()
        total = 0
        # O(n)
        for i in range(len(seats)):
            total += abs(seats[i] - students[i])
        return total
