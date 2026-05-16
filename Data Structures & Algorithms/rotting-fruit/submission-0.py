class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque()

        # get all ones and twos idxs
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        if fresh == 0:
            return 0

        mins = 0
        while queue:
            rotted = False
            for i in range(len(queue)):

                curr = queue.popleft()
                ci, cj = curr[0], curr[1]
                
                neighs = [(ci+1, cj), (ci-1, cj), (ci, cj+1), (ci, cj-1)]
                for ni, nj in neighs:

                    if ni < 0 or ni >= rows: continue
                    if nj < 0 or nj >= cols: continue
                    if grid[ni][nj] != 1: continue

                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni, nj))
                    rotted = True

            if rotted:
                mins += 1

        
        if fresh == 0:
            return mins
        
        else:
            return -1
        
        





