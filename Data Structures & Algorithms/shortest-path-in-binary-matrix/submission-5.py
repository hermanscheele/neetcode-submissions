class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        si, sj = 0, 0

        if grid[si][sj] != 0:
            return -1
        
        visited = set()
        queue = collections.deque()

        queue.append((si, sj))
        visited.add((si, sj))

        path = 1
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                i = curr[0]
                j = curr[1]

                if curr == (rows-1, cols-1):
                    return path

                neighs = [(i-1,j), (i-1,j+1), (i,j+1), (i+1,j+1), (i+1,j), (i+1,j-1), (i, j-1), (i-1, j-1)]
                for ni, nj in neighs:
                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 1 or (ni, nj) in visited:
                        continue

                    queue.append((ni,nj))
                    visited.add(curr)

            path += 1

        return -1    






