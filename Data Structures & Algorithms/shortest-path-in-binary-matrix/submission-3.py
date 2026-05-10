from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0: return -1

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        queue = deque()

        start = (0,0)
        visited.add(start)
        queue.append(start)
        
        length = 1
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr[0] == rows-1 and curr[1] == cols-1:
                    return length

                neighs = [(1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1, 0), (-1, 1), (0, 1)]

                for n in neighs:
                    di, dj = n[0], n[1]
                    x, y = curr[0] + di, curr[1] + dj

                    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 1 or (x,y) in visited: continue

                    queue.append((x,y))
                    visited.add((x, y))

            length += 1
        
        return -1