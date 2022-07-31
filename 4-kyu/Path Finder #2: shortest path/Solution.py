# Path Finder #2: shortest path

from collections import deque

def path_finder(maze):
    "BFS using queue"
    
    maze = [list(row) for row in maze.split("\n")]
    N = len(maze)
    
    start_node,end_node = ((0,0),0),((N-1,N-1)) 
    queue = deque([start_node])
    
    while queue:
        node,counter = queue.popleft()
 
        for nd in get_adjacent_nodes(maze,node,N):
            if nd == end_node:
               return counter+1
            queue.append((nd,counter+1))  
    return False                

def get_adjacent_nodes(maze,node,N):
    i,j = node[0],node[1]
    if maze[node[0]][node[1]] != ".":
        return None

    maze[i][j] = "X"
    
    if i > 0:
        yield (i-1,j)
    if i+1 < N:
        yield (i+1,j)
    if j > 0:
        yield (i,j-1)
    if j+1 < N:
        yield (i,j+1)

d = "..W.......\n.W........\n........W.\n...WW.....\nW.....WW.W\nW...WW....\n.W.W....W.\nW.W.....W.\nW.........\n.......WW."
print(path_finder(d))    
