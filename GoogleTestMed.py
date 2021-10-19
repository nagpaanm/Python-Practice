'''
Created on Oct. 10, 2021

@author: Anmol Nagpal
'''

"""
Remove Islands. Google "Medium Difficulty" coding interview challenge.

Given an nxm matrix in the form of a 2d array, remove the number of 'islands', 
where an island is represented by one or more 1's that aren't connected to 
another 1 on the border of the matrix. 

I.e. Sample Input
    [
        [1,0,0,0,0,0],
        [0,1,0,1,1,1],
        [0,0,1,0,1,0],
        [1,1,0,0,1,0],
        [1,0,1,1,0,0],
        [1,0,0,0,0,1]
    ]
    
    Sample Output
    [
        [1,0,0,0,0,0],
        [0,0,0,1,1,1],
        [0,0,0,0,1,0],
        [1,1,0,0,1,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,1]
    ]
"""

visited = []

def is_valid(i, j, matrix):
    """
    check if index errors won't occur
    """
    if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
        return True
    return False

def is_on_border(i, j, matrix):
    """
    check if matrix[i][j] is on the border of the grid
    """
    if (i == 0 or i == len(matrix) - 1) or (j == 0 or j == len(matrix[i]) - 1):
        return True
    return False

def dfs(i, j, matrix, visited):
    """
    perform depth-first-search. Keep track of visited values (or 'nodes')
    """
    if is_valid(i, j, matrix):
        if matrix[i][j] == 0:
            return
        if matrix[i][j] == 1:
            if [i,j] not in visited:
                visited.append([i,j])
                dfs(i - 1, j, matrix, visited)
                dfs(i + 1, j, matrix, visited)
                dfs(i, j - 1, matrix, visited)
                dfs(i, j + 1, matrix, visited)
    
            
def remove_islands(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            """
            only perform dfs if a 1 appears on the border of the grid
            """
            if matrix[i][j] == 1 and is_on_border(i, j , matrix):
                dfs(i, j, matrix, visited)
    
    """
    If a 1 is in the matrix and wasn't in the 'visited' list, it was not 
    reached via dfs and hence, it is an island and can be removed
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if [i,j] not in visited:
                matrix[i][j] = 0
    return matrix

if __name__ == '__main__':
    matrix = [
             [1,0,0,0,0,0],
             [0,1,0,1,1,1],
             [0,0,1,0,1,0],
             [0,1,0,1,1,1],
             [1,0,1,1,0,0],
             [1,0,0,0,0,1]
             ]
    
    """
    Sample Input
    [
        [1,0,0,0,0,0],
        [0,1,0,1,1,1],
        [0,0,1,0,1,0],
        [1,1,0,0,1,0],
        [1,0,1,1,0,0],
        [1,0,0,0,0,1]
    ]
    
    Sample Output
    [
        [1,0,0,0,0,0],
        [0,0,0,1,1,1],
        [0,0,0,0,1,0],
        [1,1,0,0,1,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,1]
    ]
    """
    
    output = remove_islands(matrix)
    for row in output:
        print(row)
    #print(visited)