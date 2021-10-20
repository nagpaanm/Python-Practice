'''
Created on Oct. 12, 2021

@author: Anmol Nagpal
'''

def dfs(graph, start, visited=None):
    """
    The first algorithm I will be discussing is Depth-First search which as 
    the name hints at, explores possible vertices (from a supplied root) down 
    each branch before backtracking. This property allows the algorithm to be 
    implemented succinctly in both iterative and recursive forms. Below is a 
    listing of the actions performed upon each visit to a node.
    
        - Mark the current vertex as being visited.
        - Explore each adjacent vertex that is not included in the visited set.
    """
    if visited is None:
        visited = []
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

def dfs2(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        for next in graph[node]:
            if next not in visited:
                visited.append(next)
                stack.append(next)
    return visited

def dfs_paths(graph, start, target, visited=[], paths=[]):
    """
    Find all possible paths between a 'start' point and an 'target' / 'end' 
    point.
    """
    if len(visited) == 0:
        visited.append(start)
    if start == target:
        paths.append(visited)
        return
    for next in graph[start]:
        if next not in visited:
            dfs_paths(graph, next, target, visited + [next], paths)
    return paths

paths_ = []
def dfs_paths2(graph, start, target, visited=[]):
    """
    Find all possible paths between a 'start' point and an 'target' / 'end' 
    point.
    
    2nd option
    """
    if len(visited) == 0:
        visited.append(start)
    if start == target:
        paths_.append(visited)
        return
    for next in graph[start]:
        if next not in visited:
            dfs_paths2(graph, next, target, visited + [next])


def dfs_paths3(graph, start, target, visited=[], paths=[]):
    """
    Find all possible paths between a 'start' point and an 'target' / 'end' 
    point.
    
    Third (3rd) option.
    """
    visited = visited + [start] #
    if start == target:
        paths.append(visited)
        return
    for next in graph[start]:
        if next not in visited:
            dfs_paths3(graph, next, target, visited, paths)
    return paths


def bfs(graph, node):
    """
    An alternative algorithm called Breath-First search provides us with the 
    ability to return the same results as DFS but with the added guarantee to 
    return the shortest-path first.
    
    Breadth-first search (BFS) is an algorithm used for tree traversal on 
    graphs or tree data structures. BFS can be easily implemented using 
    recursion and data structures like dictionaries and lists.
    
    The Algorithm
        1. Pick any node, visit the adjacent unvisited vertex, mark it as 
        visited, display it, and insert it in a queue.
        2. If there are no remaining adjacent vertices left, remove the first 
        vertex from the queue.
        3. Repeat step 1 and step 2 until the queue is empty or the desired 
        node is found.
        
        O(V+E)
    """
    visited = [node]
    queue = [node]
    
    while queue:
        s = queue.pop(0)
        for next in graph[s]:
            if next not in visited:
                visited.append(next)
                queue.append(next)
    return visited

def bfs_path(graph, start, target):
    """
    Return the shortest path between 'start' and 'target'.
    
    Note: in BFS the shortest path will always be found first (before longer
    paths) due to the use of a 'queue'.
    """
    if start == target:
        return [start]
    paths = []
    visited = [start]
    queue = [start]
    
    while queue:
        s = queue.pop(0)
        for next in graph[s]:
            if next not in visited:
                if s == start:
                    if next == target:
                        return [s, next]
                    else:
                        paths.append([s, next])
                else:
                    l = []
                    for lst in paths:
                        for item in lst:
                            if item == s:
                                if next == target:
                                    return lst + [next]
                                else:
                                    l = lst + [next]
                    if l:
                        paths.append(l)
                visited.append(next)
                queue.append(next)
            print(paths)
    return []

def bfs_path2(graph, start, target):
    """
    Return the shortest path between 'start' and 'target'.
    
    Note: in BFS the shortest path will always be found first (before longer
    paths) due to the use of a 'queue'.
    """
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == target:
            return path
        for next in graph[node]:
            new_path = list(path)
            new_path.append(next)
            queue.append(new_path)

def bfs_path3(graph, start, target):
    """
    Return the shortest path between 'start' and 'target'.
    
    Note: in BFS the shortest path will always be found first (before longer
    paths) due to the use of a 'queue'.
    """
    if start == target:
        return [start]
    visited = [start]
    queue = [[start]]   #2d array (i.e. list of lists)
    
    while queue:
        path = queue.pop(0) #list
        node = path[-1] #either first index if len = 1, or last index if len > 1
        if node == target:
            return path
        for next in graph[node]:
            if next not in visited:
                visited.append(next)
                queue.append(path + [next])
    #no path
    return []
if __name__ == '__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    
    print("dfs ",dfs(graph, 'C'))
    print("dfs2 ", dfs2(graph, 'A'))
    print((dfs_paths(graph, 'A', 'F')))
    
    dfs_paths2(graph, 'A', 'F')
    #print(paths_)
    #print((dfs_paths3(graph, 'A', 'F')))
    
    graph2 = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }
    
    graph3 = {
        'A' : ['B','C'],
        'B' : ['A', 'D', 'E'],
        'C' : ['A', 'F'],
        'D' : ['B'],
        'E' : ['B', 'F'],
        'F' : ['C', 'E']
    }
    
    print(bfs(graph3, 'A')) # A B C D E F
    print(dfs(graph3, 'A')) # A B D E F C
    print(bfs_path(graph, 'A', 'E'))
    print(bfs_path2(graph, 'A', 'F'))
    print(bfs_path3(graph, 'A', 'F'))