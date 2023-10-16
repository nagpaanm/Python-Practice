'''
Created on Feb. 4, 2023

@author: Anmol Nagpal
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mapping = {}
        for pair in edges:
            if pair[0] in mapping:
                mapping[pair[0]].append(pair[1])
            else:
                mapping[pair[0]] = [pair[1]]
            # bi-directional
            if pair[1] in mapping:
                mapping[pair[1]].append(pair[0])
            else:
                mapping[pair[1]] = [pair[0]]
        #DFS
        visited = {source}
        queue = [source]
        while (len(queue) != 0):
            curr = queue[0]
            del queue[0]
            if(curr == destination):
                return True
            if curr in mapping:
                path = mapping[curr] 
            else:
                path = []
            for val in path:
                if val not in visited:
                    queue.append(val)
                    visited.add(val)
        return destination in visited
