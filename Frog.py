'''
Created on Oct. 19, 2021

@author: Anmol Nagpal
'''

"""
Medium difficulty recursion question:

There are 10 stones in a line leading across the river, 
separated by 1 foot. He can either jump to the next stone or jump over a stone, 
and if he jumps over a stone he must land on the next one. 
The furthest he can jump is 2 feet. Also, he always moves forward 
(toward the other side of the river). 

In how many different ways can he cross the river?
"""


def frog_jumps(n, c=0):
    if n > 1:
        c += frog_jumps(n - 1, c) + frog_jumps(n - 2, c)
    else:
        return 1
    return c

def frog_jumps_memoize(n, arr, c=0):
    """
    Using a memoized solution (dynammic programming).
    
    O(n) runtime.
    """
    if arr[n] != None:
        return arr[n]
    if n > 1:
        c += frog_jumps_memoize(n - 1, arr, c) + frog_jumps_memoize(n - 2, arr, c)
    else:
        return 1
    arr[n] = c
    return c

def frog_jumps_bottom_up(n):
    """
    Using a bottom-up approach. Will not run into 'maximum recursion depth
    exceeded' problems.
    
    O(n) runtime.
    """
    if n <= 1:
        return 1
    bottom_up = [None for _ in range(n + 1)]
    bottom_up[1] = 1
    bottom_up[2] = 2
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]

if __name__ == '__main__':
    n = 1000
    #print(frog_jumps(n)) 
    #print(frog_jumps_memoize(n, [None for _ in range(n + 1)]))
    print(frog_jumps_bottom_up(n))