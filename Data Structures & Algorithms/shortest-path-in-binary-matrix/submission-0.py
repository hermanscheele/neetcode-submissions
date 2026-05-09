from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        length = 1
        visited = set()
        queue = deque()

        start = (0,0)
        if grid[start[0]][start[1]] == 1: return -1

        visited.add(start)
        queue.append(start)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                
                if curr[0] == rows-1 and curr[1] == cols-1: 
                    return length

                neighs = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
                for n in neighs:
                    di = n[0]
                    dj = n[1]

                    x = curr[0] + di
                    y = curr[1] + dj

                    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 1 or (x,y) in visited: continue
                    

                    visited.add((x,y))
                    queue.append((x,y))

            length += 1


        return -1